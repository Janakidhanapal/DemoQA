import time
from Selenium.DemoQA.reusablefiles.General import *


def test_links():
    driver = invoke_browser()
    click_card(driver, "Elements")
    show_element_list(driver, "Elements")
    select_submenu_item(driver, "Links")
    link_name = "Bad Request"
    driver.find_element(By.XPATH, f'//a[text()="{link_name}"]').click()
    handles = driver.window_handles
    if len(handles) > 1:
        driver.switch_to.window(handles[1])
        if driver.title == "ToolsQA":
            print("Valid webpage is opened")
            driver.close()
        driver.switch_to.window(handles[0])
    else:
        print(driver.find_element(By.ID, "linkResponse").text)
    time.sleep(8)
    tear_down(driver)
