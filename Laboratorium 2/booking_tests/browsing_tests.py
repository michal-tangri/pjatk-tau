from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_hotel_browsing(driver):
    driver.get("https://www.booking.com/")
    driver.find_element_by_id("ss").send_keys("Sopot")
    driver.find_element_by_css_selector(".xp__input-group.xp__guests").click()
    driver.find_elements_by_css_selector(".bui-button.bui-button--secondary.bui-stepper__add-button")[2].click()
    driver.find_element_by_xpath(xpath='//label[@for="sb_travel_purpose_checkbox"]').click()
    driver.find_element_by_xpath(xpath='//button[@data-sb-id="main"]').click()
    checkin_date = WebDriverWait(driver=driver, timeout=5).until(expected_conditions.presence_of_element_located((By.XPATH, '//td[@data-date="2021-04-29"]')))
    checkin_date.click()
    driver.find_element_by_css_selector(".sb-searchbox__button ").click()
    driver.find_element_by_css_selector(".txp-cta.bui-button.bui-button--primary.sr_cta_button").click()

    return "Browsing hotels test for Booking.com using '" + driver.name + "' driver was successful."
    

def test_attractions_browsing(driver):
    driver.get("https://www.booking.com/")
    try:
        WebDriverWait(driver=driver, timeout=5).until(expected_conditions.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()
    except:
        print()
    driver.find_element_by_xpath(xpath='//a[@data-decider-header="attractions"]').click()
    driver.find_element_by_name(name="query").send_keys("PJATK")
    WebDriverWait(driver=driver, timeout=5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.styled-bui-1h7anqn'))).click()
    WebDriverWait(driver=driver, timeout=5).until(expected_conditions.presence_of_element_located((By.XPATH, '//div[@data-testid="datepicker"]'))).click()
    driver.find_element_by_xpath(xpath='//span[@aria-label="31 marzec 2021"]').click()
    WebDriverWait(driver=driver, timeout=5).until(expected_conditions.presence_of_element_located((By.XPATH, '//button[@data-testid="select-ticket"]'))).click()
    WebDriverWait(driver=driver, timeout=5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.bui-button.styled-bui-1xok4pd.bui-button--secondary'))).click()
    driver.find_element_by_css_selector(".bui-button.bui-button--primary.bui-button--wide").click()
    error_msg = driver.find_element_by_css_selector(".bui-text.bui-text--variant-body_2.styled-bui-17ijryf").text

    if (error_msg == "Wybierz co najmniej jeden bilet"):
        return "Browsing test for Booking.com using '" + driver.name + "' driver was successful."
    
    return "Browsing attractions test for Booking.com using '" + driver.name + "' driver failed."
    

if __name__ == "__main__":
    print(test_hotel_browsing(webdriver.Chrome(executable_path="../drivers/chromedriver.exe")))
    print(test_hotel_browsing(webdriver.Edge(executable_path="../drivers/msedgedriver.exe")))
    print(test_hotel_browsing(webdriver.Firefox(executable_path="../drivers/geckodriver.exe"))) 