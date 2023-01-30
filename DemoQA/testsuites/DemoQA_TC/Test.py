from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.find_elements(By.XPATH, "//div[.='Full Name']//input")
driver.find_element(By.XPATH, "//div[.='Email']//input")
driver.find_element(By.XPATH, "//div[.='Current Address']//textarea")
driver.find_element(By.XPATH, "//div[.='Permanent Address']//textarea")
