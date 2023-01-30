from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scroll_into_view(driver: webdriver, element: WebElement):
    driver.execute_script('arguments[0].scrollIntoView()', element)
    return element


def wait_until_element_visible(driver: webdriver, locator: tuple, timeout: int):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
    except TimeoutError:
        driver.close()
        driver.quit()
