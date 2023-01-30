import time

import Selenium.DemoQA.reusablefiles.ElementHandling as EH
from Selenium.DemoQA.reusablefiles.General import *
from pywinauto.application import Application

driver = invoke_browser()
click_card(driver, "Elements")
show_element_list(driver, "Elements")
select_submenu_item(driver, "Upload and Download")
EH.wait_until_element_visible(driver, (By.XPATH, '//input[@id="uploadFile"]'), 10)
ele_upload_file = driver.find_element(By.XPATH, '//input[@id="uploadFile"]')
driver.execute_script('arguments[0].click();', ele_upload_file)
# ele_upload_file.send_keys("C:/Users/Vigneshwaran/Downloads/sampleFile.jpeg")

# PyWinAuto
app = Application().connect(title='Open', timeout=5)
app.Open.type_keys(r"C:\Users\Vigneshwaran\Downloads\sampleFile.jpeg")
time.sleep(3)
app.Open.Open.click()

time.sleep(10)
tear_down(driver)
