from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Z jakiegoś powodu bardzo długo czeka na RODO, podczas gdy w drugim teście jest instant
def test_telemegazyn_tv_programme():
    driver = webdriver.Chrome(
        executable_path="./drivers/chromedriver.exe", service_log_path='NUL')
    driver.get("https://www.telemagazyn.pl/")
    rodo_button = WebDriverWait(driver=driver, timeout=3).until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[@id="didomi-notice-agree-button"]')))
    rodo_button.click()
    tv_programme_link = driver.find_element_by_xpath('//*[@id="gora"]/div[1]/div/nav/ul/li[1]')
    tv_programme_link.click()
    all_day_option = driver.find_element_by_xpath('//*[@id="filtry"]/div/div[2]/a[5]')
    all_day_option.click()
    polsat = driver.find_element_by_xpath('//*[@id="programTV"]/table[1]/thead/tr/th[4]')
    polsat.click()
    sleep(3)

def test_onet_tv_programme():
    driver = webdriver.Chrome(
        executable_path="./drivers/chromedriver.exe", service_log_path='NUL')
    driver.get("https://onet.pl/")
    rodo_button = WebDriverWait(driver=driver, timeout=3).until(expected_conditions.presence_of_element_located(
        (By.XPATH, '//*[@id="pageMainContainer"]/div[5]/div[1]/div[2]/div/div[3]/button[2]')))
    rodo_button.click()
    tv_programme_link = driver.find_element_by_xpath('//*[@id="SuperWidgetModule"]/ul/li[2]/a')
    tv_programme_link.click()
    search_input = driver.find_element_by_xpath('//*[@id="searchQuery"]')
    search_input.send_keys('HBO')
    search_input.send_keys(Keys.ENTER)
    hbo_2_hd_link = driver.find_element_by_xpath('/html/body/div[3]/ul[2]/li[4]')
    hbo_2_hd_link.click()
    sleep(3)

if __name__ == "__main__":
    test_onet_tv_programme()
    test_telemegazyn_tv_programme()
