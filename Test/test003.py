# coding = utf-8
import time

from selenium import webdriver;
from selenium.webdriver.common.by import By

tele = 17616108350
password = "lylelove"
driver = webdriver.Chrome()

driver.get("https://www.icourse163.org/")

driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div/div[1]/div[3]/div[3]/div").click()
driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div/div/div/div/div[2]/span").click()
driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[1]/ul/li[2]").click()

iframe = driver.find_element(By.XPATH,"/html/body/div[13]/div[2]/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[2]/div/iframe")
driver.switch_to.frame(iframe)
driver.find_element(By.ID, "phoneipt").send_keys(tele)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div/div[4]/div[2]/input[2]").send_keys(password)
driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[2]/form/div/div[6]/a").click()

# driver.switch_to.default_content()
time.sleep(10)
driver.find_element(By.ID, "privacy-ok").click()
driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div/div/div[1]/div[3]/div[4]/div").click()
driver.find_element(By.XPATH,)

