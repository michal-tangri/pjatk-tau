from socket import SO_KEEPALIVE
from time import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_booking_login(driver):
    driver.get("https://www.booking.com/")
    driver.find_element_by_css_selector(".bui-button.bui-button--secondary.js-header-login-link").click()
    email_field = driver.find_element_by_id("username")
    email_field.send_keys("obq01390@lcdvd.com")
    email_field.send_keys(Keys.ENTER)
    password_field = WebDriverWait(driver=driver, timeout=5).until(expected_conditions.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("VaXb94U?7@/xjnp")
    password_field.send_keys(Keys.ENTER)

    try:
        user_field = WebDriverWait(driver=driver, timeout=5).until(expected_conditions.presence_of_element_located((By.ID , "profile-menu-trigger--title")))
    except:
        return "Login test for Booking.com using '" + driver.name + "' driver failed. Login unsuccessful."

    if user_field.text == "Paweł Pavlov":
        return "Login test for Booking.com using '" + driver.name + "' driver was successful."
    
    return "Login test for Booking.com using '" + driver.name + "' driver failed. Wrong or missing account information."
    

if __name__ == "__main__":
    print(test_booking_login(webdriver.Chrome(executable_path="../drivers/chromedriver.exe")))
    print(test_booking_login(webdriver.Edge(executable_path="../drivers/msedgedriver.exe")))
    print(test_booking_login(webdriver.Firefox(executable_path="../drivers/geckodriver.exe")))