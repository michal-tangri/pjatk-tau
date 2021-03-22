from selenium import webdriver
from selenium.webdriver.common import desired_capabilities
from ciapkowo_tests import simple_tests

from selenium import webdriver

if __name__ == "__main__":

    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True

    options = webdriver.ChromeOptions()
    options.add_argument('ignore-certificate-errors')

    capabilities = webdriver.DesiredCapabilities().EDGE
    capabilities['acceptSslCerts'] = True

    drivers = [
        webdriver.Chrome(executable_path="./drivers/chromedriver.exe", service_log_path='NUL', options=options),
        webdriver.Edge(executable_path="./drivers/msedgedriver.exe", service_log_path='NUL', capabilities=capabilities),
        webdriver.Firefox(executable_path="./drivers/geckodriver.exe", service_log_path='NUL', firefox_profile=profile)
    ]
    for driver in drivers:
        # print(simple_tests.test_pet_browsing(driver))
        # print(simple_tests.test_pet_adoption(driver))
        print(simple_tests.test_donating(driver))
        