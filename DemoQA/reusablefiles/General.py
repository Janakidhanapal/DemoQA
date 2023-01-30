from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from DemoQA.reusablefiles.ElementHandling import scroll_into_view


def invoke_browser() -> webdriver:
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    return driver


def click_card(driver: webdriver, card: str):
    a_element = driver.find_element(By.XPATH, f"//h5[text()= '{card}']")
    scroll_into_view(driver, a_element)
    a_element.click()


def show_element_list(driver: webdriver, item_menu):
    dd_collapse = driver.find_element(By.XPATH, f"//span[starts-with(.,'{item_menu}')]//parent::div[@class='element-group']/div")
    if "show" not in dd_collapse.get_attribute("class"):
        dd_collapse.click()


def select_submenu_item(driver: webdriver, submenu_item: str):
    sub_item = driver.find_element(By.XPATH, f"//span[starts-with(.,'{submenu_item}')]")
    scroll_into_view(driver, sub_item)
    sub_item.click()

def tear_down(driver):
    driver.close()
    driver.quit()

# class Car:
#     def __init__(self, name: str, year_of_purchase, rate):
#         self.name = name
#         self.year_of_purchase = year_of_purchase
#         self.rate = rate
#
#     def print_details(self):
#         print(f'Car detail - {self.name} | {self.year_of_purchase} | {self.rate}')
#
#
# car1 = Car("Maruti Alto", "2000", "400000")
# car1.print_details()
