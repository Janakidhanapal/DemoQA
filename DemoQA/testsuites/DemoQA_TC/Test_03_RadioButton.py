import time
import Selenium.DemoQA.reusablefiles.ElementHandling as EH
from Selenium.DemoQA.reusablefiles.General import *


def test_radiobutton():
    driver = invoke_browser()
    click_card(driver, "Elements")
    show_element_list(driver, "Elements")
    time.sleep(1)
    select_submenu_item(driver, "Radio Button")
    question = ["Do you like the site?", "How are you?"]
    EH.wait_until_element_visible(driver, (By.XPATH, "//div[@class='mb-3']"), 9)
    assert driver.find_element(By.XPATH, "//div[@class='mb-3']").text in question, "Question is not available"
    answer = "No"
    btn_status = driver.find_element(By.XPATH, f"//label[text()='{answer}']").get_attribute('class')
    assert "disabled" not in btn_status, "Button is in Disabled state"
    driver.find_element(By.XPATH, f"//label[text()='{answer}']").click()
    assert driver.find_element(By.XPATH,
                               f"//label[text()='{answer}']/preceding-sibling::input").is_selected(), f"{answer} is not selected"
    assert driver.find_element(By.XPATH,
                               "//span[@class = 'text-success']").text == answer, "Given and selected buttons are not equal"
    time.sleep(2)
    tear_down(driver)
