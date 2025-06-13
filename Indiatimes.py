# -*- coding: utf-8 -*-
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random
import requests
import urllib.parse


# === Device settings ===
devices = [
    {"name": "iPhone X", "width": 375, "height": 812, "mobile": True},
    {"name": "Pixel 2", "width": 411, "height": 731, "mobile": True},
    {"name": "iPad", "width": 768, "height": 1024, "mobile": True},
]


for device in devices:
    print(f"Opening as {device['name']}")
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--remote-debugging-port=9222")

    if device["mobile"]:
        mobile_emulation = {
            "deviceMetrics": {
                "width": device["width"],
                "height": device["height"],
                "pixelRatio": 3.0
            },
            "userAgent": (
                "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) "
                "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 "
                "Mobile/15E148 Safari/604.1"
            )
        }
        options.add_experimental_option(
            "mobileEmulation", mobile_emulation)
    else:
        options.add_argument(
            f"--window-size={device['width']},{device['height']}")

    try:
        # path = r"C:\WebDriver\bin\chromedriver.exe"
        path = "/usr/bin/chromedriver"
        service = Service(executable_path=path)
        driver = webdriver.Chrome(service=service, options=options)
        urls = [
            "https://bharatfitguru.blogspot.com/p/hello-world.html",
        ]

        url = random.choice(urls)

        driver.get(str(url))
        print('wait for 20 seconds')
        time.sleep(20)
        driver.refresh()
        time.sleep(20)
        driver.quit()

    except Exception as e:
        pass

# Optional delay between full cycles, e.g., 60 seconds
print("Cycle complete, waiting 5 seconds before next run...")
time.sleep(5)
