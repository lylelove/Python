# encoding:utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

account = '20190611509'
password = 'lylelove2000'

driver = webdriver.Chrome()
driver.get("http://jw.sdufe.edu.cn/")

driver.find_element(By.ID, "userAccount").send_keys(account)
driver.find_element(By.ID, "userPassword").send_keys(password)
iframe0 = (By.ID,"Frame0")
WebDriverWait(driver, 60, 0.5).until(expected_conditions.presence_of_element_located(iframe0))
iframe0 = driver.find_element(By.ID,"Frame0")
driver.switch_to.frame(iframe0)
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div/div/div[5]/p").click()
time.sleep(2)
iframe1 = driver.find_element(By.ID,"notSession")
driver.switch_to.frame(iframe1)
driver.find_element(By.LINK_TEXT, "进入评价").click()
