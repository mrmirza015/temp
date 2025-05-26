# -*- coding: utf-8 -*-
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# === Device settings ===
devices = [
    {"name": "iPhone X", "width": 375, "height": 812, "mobile": True},
    {"name": "Pixel 2", "width": 411, "height": 731, "mobile": True},
    {"name": "iPad", "width": 768, "height": 1024, "mobile": True},
    {"name": "Desktop 1366x768", "width": 1366, "height": 768, "mobile": False},
    {"name": "Desktop 1920x1080", "width": 1920, "height": 1080, "mobile": False}
]

url = "https://adsonick.blogspot.com/2025/05/stakelink4.html"

for device in devices:
    print(f"Opening as {device['name']}")
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--headless=new")

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
        options.add_experimental_option("mobileEmulation", mobile_emulation)
    else:
        options.add_argument(
            f"--window-size={device['width']},{device['height']}")

    try:
        # Ensure chromedriver path is correct
        # path = r"C:\WebDriver\bin\chromedriver.exe"
        path = "/usr/bin/chromedriver"
        service = Service(executable_path=path)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)
        print('wait for 4 seconds')
        time.sleep(4)
        driver.quit()

    except Exception as e:
        print(f"Error: {e}")
        os._exit(1)
