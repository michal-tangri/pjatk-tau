import logging
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] (%(levelname)s) - %(message)s", datefmt="%d/%m/%Y %H:%M:%S")

def test_telemegazyn_tv_programme():
    driver = webdriver.Chrome(
        executable_path="./drivers/chromedriver.exe", service_log_path='NUL')
    logging.info("Webdriver initialized")

    driver.get("https://www.telemagazyn.pl/")
    logging.info("Web page opened")

    logging.warning("Waiting for RODO confimation button - may result in an error")
    try:
        rodo_button = WebDriverWait(driver=driver, timeout=3).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="didomi-notice-agree-button"]')))
        rodo_button.click()
    except TimeoutException:
        logging.error("Error while waiting for RODO confirmation button")

    tv_programme_link = driver.find_element_by_xpath('//*[@id="gora"]/div[1]/div/nav/ul/li[1]')
    logging.info("Choosing TV Programme link")
    tv_programme_link.click()

    all_day_option = driver.find_element_by_xpath('//*[@id="filtry"]/div/div[2]/a[5]')
    logging.info("Choosing all day option")
    all_day_option.click()
    polsat = driver.find_element_by_xpath('//*[@id="programTV"]/table[1]/thead/tr/th[4]')
    logging.info("Choosing POLSAT")
    polsat.click()
    logging.info("Test successful")
    sleep(3)
    

def test_onet_tv_programme():
    driver = webdriver.Chrome(
        executable_path="./drivers/chromedriver.exe", service_log_path='NUL')

    logging.info("Webdriver initialized")
    driver.get("https://onet.pl/")
    logging.info("Web page opened")

    logging.warning("Waiting for RODO confimation button - may result in an error")
    try:
        rodo_button = WebDriverWait(driver=driver, timeout=3).until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[@id="pageMainContainer"]/div[5]/div[1]/div[2]/div/div[3]/button[2]')))
        rodo_button.click()
    except TimeoutException:
        logging.error("Error while waiting for RODO confirmation button")

    tv_programme_link = driver.find_element_by_xpath('//*[@id="SuperWidgetModule"]/ul/li[2]/a')
    logging.info("Choosing TV Programme link")
    tv_programme_link.click()

    search_input = driver.find_element_by_xpath('//*[@id="searchQuery"]')
    logging.info("Searching for HBO using input field")
    search_input.send_keys('HBO')
    search_input.send_keys(Keys.ENTER)

    hbo_2_hd_link = driver.find_element_by_xpath('/html/body/div[3]/ul[2]/li[4]')
    logging.info("Choosing HBO 2 HD")
    hbo_2_hd_link.click()
    logging.info("Test successful")
    sleep(3)

if __name__ == "__main__":
    test_telemegazyn_tv_programme()
    test_onet_tv_programme()
