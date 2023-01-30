import time
import DemoQA.reusablefiles.ElementHandling as EH
from DemoQA.reusablefiles.General import *


def test_textbox():
    driver = invoke_browser()
    click_card(driver, "Elements")
    show_element_list(driver, "Elements")
    select_submenu_item(driver, "Text Box")
    userName = EH.wait_until_element_visible(driver, (By.ID, "userName"), 5)
    userName.send_keys("name")
    userEmail = driver.find_element(By.ID, "userEmail")
    userEmail.send_keys("janaki@gmail.com")
    cAddress = driver.find_element(By.ID, "currentAddress")
    cAddress.send_keys("jan_address")
    pAddress = driver.find_element(By.ID, "permanentAddress")
    pAddress.send_keys("Permanent Address")
    EH.scroll_into_view(driver, driver.find_element(By.ID, "submit")).click()
    EH.wait_until_element_visible(driver, (By.XPATH, "//div[@id='output']//p"), 5)
    given_user_input = driver.find_elements(By.XPATH, "//div[@id='output']//p")
    for i in range(1, len(given_user_input) + 1):
        output_text = driver.find_element(By.XPATH, f"//div[@id='output']//p[{i}]").text
        li = output_text.split(":")
        if li[0] == "Name":
            assert userName.get_attribute("value") == li[1], "Username not equal"
        elif li[0] == "Email":
            assert userEmail.get_attribute("value") == li[1], "Email not equal"
        elif li[0] == "Current Address ":
            assert cAddress.get_attribute("value") == li[1], "address not equal"
        elif li[0] == "Permananet Address ":
            assert pAddress.get_attribute("value") == li[1], "Permanent address not equal"

    time.sleep(5)
    tear_down(driver)
