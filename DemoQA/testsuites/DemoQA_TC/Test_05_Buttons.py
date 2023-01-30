import time
from selenium.webdriver.common.action_chains import ActionChains
from Selenium.DemoQA.reusablefiles.General import *


def test_buttons():
    driver = invoke_browser()
    click_card(driver, "Elements")
    show_element_list(driver, "Elements")
    select_submenu_item(driver, "Buttons")

    button = driver.find_element(By.XPATH, '//button[text()="Click Me"]')
    actionChains = ActionChains(driver)
    if button.text == "Double Click Me":
        actionChains.double_click(button).perform()
    elif button.text == "Right Click Me":
        actionChains.context_click(button).perform()
    else:
        driver.find_element(By.XPATH, f'//button[text()="{button.text}"]').click()
    assert driver.find_element(By.XPATH, '//div[@class="mt-4"]/following-sibling::div/following::p'), "Button was not clicked"
    time.sleep(10)
    tear_down(driver)