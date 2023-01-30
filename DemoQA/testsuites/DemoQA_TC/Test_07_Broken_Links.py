import requests
from Selenium.DemoQA.reusablefiles.General import *


def test_brokenlinks():
    driver = invoke_browser()
    click_card(driver, "Elements")
    show_element_list(driver, "Elements")
    select_submenu_item(driver, "Broken Links - Images")
    image_list = driver.find_elements(By.XPATH, "//div/p/following-sibling::img")
    print(len(image_list))
    for img in image_list:
        response = requests.get(img.get_attribute('src'), stream=True)
        print(img.get_attribute('naturalWidth'))
        if img.get_attribute("naturalWidth") == '0':
            print("The image is broken")

    tear_down(driver)
