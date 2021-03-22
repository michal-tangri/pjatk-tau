from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_pet_browsing(driver):
    driver.get("https://www.ciapkowo.pl/")
    driver.find_element_by_xpath('//*[@id="menu-item-226"]/a').click()
    driver.find_element_by_xpath('//label[@for="plec1"]').click()
    driver.find_element_by_xpath('//*[@id="wiek_od"]').send_keys(1)
    driver.find_element_by_xpath('//*[@id="wiek_do"]').send_keys(3)
    driver.find_element_by_xpath('//label[@for="wielkosc2"]').click()
    driver.find_element_by_xpath('//label[@for="aktywnosc2"]').click()
    driver.find_element_by_css_selector(".btn.btn-primary").click()

    return "Browsing pets test for Ciapkowo.pl using '" + driver.name + "' driver was successful."
    
def test_pet_adoption(driver):
    driver.get("https://www.ciapkowo.pl/")
    driver.find_element_by_xpath('//*[@id="menu-item-227"]/a').click()
    driver.find_elements_by_css_selector(".btn.btn-primary.stretched-link")[3].click()
    driver.find_element_by_xpath('//*[@id="rodzaj-opiekuna"]').click()
    driver.find_element_by_xpath('//*[@id="rodzaj-opiekuna"]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="imie-firma"]').send_keys("PJATK")
    driver.find_element_by_xpath('//*[@id="mail"]').send_keys("adres@pjwstk.edu.pl")
    driver.find_element_by_xpath('//*[@id="phone"]').send_keys("694202137")
    driver.find_element_by_xpath('//*[@id="accept-show-name"]').click()
    driver.find_element_by_xpath('//*[@id="accept-law"]').click()

    return "Adopting a pet test for Ciapkowo.pl using '" + driver.name + "' driver was successful."

def test_donating(driver):
    driver.get("https://www.ciapkowo.pl/")
    driver.find_element_by_xpath('//*[@id="menu-item-dropdown-516"]/span').click()
    driver.find_element_by_xpath('//*[@id="menu-item-519"]/a/span').click()
    driver.find_element_by_xpath('//label[@for="rodzaj1"]').click()
    driver.find_element_by_xpath('//label[@for="plec2"]').click()
    driver.find_element_by_xpath('//label[@for="wielkosc3"]').click()
    driver.find_element_by_css_selector(".btn.btn-primary").click()
    driver.find_elements_by_css_selector(".btn.btn-primary.stretched-link")[2].click()
    driver.find_element_by_xpath('//*[@id="rodzaj-opiekuna"]').click()
    driver.find_element_by_xpath('//*[@id="rodzaj-opiekuna"]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="imie-firma"]').send_keys("PJATK")
    driver.find_element_by_xpath('//*[@id="mail"]').send_keys("adres@pjwstk.edu.pl")
    driver.find_element_by_xpath('//*[@id="phone"]').send_keys("694202137")
    driver.find_element_by_xpath('//*[@id="accept-show-name"]').click()
    driver.find_element_by_xpath('//*[@id="accept-law"]').click()


    return "Donating test for Ciapkowo.pl using '" + driver.name + "' driver was successful."