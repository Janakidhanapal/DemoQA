import time
import Selenium.DemoQA.reusablefiles.ElementHandling as EH
from Selenium.DemoQA.reusablefiles.General import *


def test_checkbox():
    driver = invoke_browser()
    click_card(driver, "Elements")
    show_element_list(driver, "Elements")
    select_submenu_item(driver, "Check Box")
    # Click the plus button in Check Box page
    EH.wait_until_element_visible(driver, (By.XPATH, "//button[@class='rct-option rct-option-expand-all']"), 5).click()
    path = 'Home/Documents/WorkSpace/Veu'
    directory = path.split('/')
    ele_treenode = driver.find_element(By.ID, 'tree-node')
    for i in range(len(directory) - 1):
        ele_treenode = ele_treenode.find_element(By.XPATH, f"//ol//span[text()='{directory[i]}']/ancestor::li[1]")
    ele_treenode.find_element(By.XPATH, f"//span[text()='{directory[-1]}']").click()
    time.sleep(9)
    assert ele_treenode.find_element(By.XPATH,
                                     f"//span[text()='{directory[-1]}']//preceding-sibling::input").is_selected(), "CheckBox is not checked"
    time.sleep(5)
    tear_down(driver)
