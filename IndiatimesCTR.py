# in this code i have successfully_clicked_on_safeframe_passback_tags using id
# -*- coding: utf-8 -*-
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random
import requests
import urllib.parse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

for i in range(3):
    # path = r"C:\WebDriver\bin\chromedriver.exe"
    path = "/usr/bin/chromedriver"
    service = Service(executable_path=path)
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(service=service, options=options)
    url = 'https://bharatfitguru.blogspot.com/p/ctr.html'
    driver.get(url)
    elem = driver.find_element(
        By.ID, "google_ads_iframe_/7176/Indiatimes/IT_Partner_passback/IT_OTH_Passback_3_300x250_0__container__")
    print(f'the element is {elem.get_attribute("innerHTML")}')
    time.sleep(10)
    print('wait for 10 sec')
    elem.click()
    print('clicked')
    time.sleep(10)
    print('wait for 10 sec')
    driver.switch_to.window(driver.window_handles[-1])
    print('window switched')
    time.sleep(random.randint(25, 40))
    print('wait for 25-40 sec')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    print('scroll down')
    driver.refresh()
    print('refereshed')
    time.sleep(10)
    print('wait for 10 sec')
    driver.refresh()
    print('refereshed')
    time.sleep(10)
    print('wait for 10 sec')

    print('closed')
    driver.close()
