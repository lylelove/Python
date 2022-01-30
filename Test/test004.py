from telnetlib import EC

import selenium;
from selenium.webdriver.chrome import webdriver
# coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()

driver.get("https://www.bilibili.com/account/history")

driver.find_element(By.LINK_TEXT, "登录").click()
login = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/div[3]/div[2]/div[6]/span/div[2]/span/span")
WebDriverWait(driver, 60, 0.5).until(expected_conditions.presence_of_element_located(login))
driver.find_element(By.XPATH,
                    "/html/body/div[2]/div/div[1]/div[1]/div/div[3]/div[2]/div[6]/span/div[2]/span/span").click()
time.sleep(1)
driver.switch_to.window(driver.window_handles[1])


def sort(ar):
    dict = {}
    dict = dict.fromkeys(ar, 0)
    ca = list(dict)
    for num in range(0, len(ca)):
        for i in range(0, len(ar)):
            if ca[num] == ar[i]:
                dict[ca[num]] = dict[ca[num]] + 1
    return str(dict)


def ex_element(ele):
    try:
        driver.find_element(By.XPATH, ele)
        exc = True
        return exc
    except:
        exc = False
        return exc


def counting():
    results = []
    num = 1
    flag = True
    while flag:
        try:
            li = "/html/body/div[2]/div/div[3]/ul/li[" + str(num) + "]"
            driver.find_element(By.XPATH, li)
            try:
                record = "/html/body/div[2]/div/div[3]/ul/li[" + str(num) + "]/div[2]/div[2]/div/span/span"
                target = driver.find_element(By.XPATH, record)
                a = target.get_attribute('innerHTML')
                if a != '':
                    results.append(a)
                num=num+1
            except:
                num=num+1
        except:
            driver.execute_script("window.scrollBy(0,10000)")
            try:
                li = "/html/body/div[2]/div/div[3]/ul/li[" + str(num) + "]"
                lir = (By.XPATH, li)
                WebDriverWait(driver, 10, 0.05).until(expected_conditions.presence_of_element_located(lir))
                driver.find_element(By.XPATH, li)
            except:
                flag = False
                print(num)
            # record = "/html/body/div[2]/div/div[3]/ul/li[" + str(num) + "]/div[2]/div[2]/div/span/span"
            # target = driver.find_element(By.XPATH, record)
            # a = target.get_attribute('innerHTML')
            # results.append(a)
            # num = num + 1
            # print(num)

    return results


re = counting()

print(sort(re))
