from selenium import webdriver
from booking_tests import auth_tests
from booking_tests import browsing_tests

from selenium import webdriver

if __name__ == "__main__":
    drivers = [
        webdriver.Chrome(executable_path="./drivers/chromedriver.exe", service_log_path='NUL'),
        webdriver.Edge(executable_path="./drivers/msedgedriver.exe", service_log_path='NUL'),
        webdriver.Firefox(executable_path="./drivers/geckodriver.exe", service_log_path='NUL')
    ]
    for driver in drivers:
        print(auth_tests.test_booking_login(driver))
        print(browsing_tests.test_attractions_browsing(driver))
        print(browsing_tests.test_hotel_browsing(driver))
        driver.close()
        