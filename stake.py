# -*- coding: utf-8 -*-
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import random
import requests
import urllib.parse


sr_mobile_arr = [
    '360×800'
]

baseUrl = 'https://analytics.google.com/g/collect?'
version = '2'
npa = '0'
dma = '0'
tag_exp = '0'
ul = 'en-us'
dr = ''
dl = 'https://example.com/'
dt = 'example'

uam_arr = [
    'SM-G955U']

gtm = "45je4cc1v9108524162za200"
gcd = "13l3l3l3l1l1"


def generate_urls():
    uri_dl = urllib.parse.quote(dl)
    uri_dt = urllib.parse.quote(dt)
    uri_dr = urllib.parse.quote(dr)
    p = random.randint(0, 2147483647)
    sid = int(time.time())
    cid = f"{100000000 + random.randint(0, 1) + random.randint(0, 100000000)}.{sid}"
    tfd1 = 100 + random.randint(0, 4000)
    tfd2 = tfd1 + random.randint(0, 400)
    uab = ''
    uamb = ''
    uap = ''
    uam = ''
    uafvl = ''
    sr = ''
    uaa = ''
    ir = ''
    isMobile = True
    if isMobile:
        sr = random.choice(sr_mobile_arr)
        uap = 'Android'
        uamb = '1'
        uam = urllib.parse.quote(random.choice(uam_arr))

    tracker = f"{baseUrl}v={version}&tid=G-WZXPX61NKF&gtm={gtm}&_p={p}&gcd={gcd}&npa={npa}&dma={dma}&tag_exp={tag_exp}&cid={cid}&ul={ul}&sr={sr}&ir={ir}&uaa={uaa}&uab={uab}&uafvl={uafvl}&uamb={uamb}&uam={uam}&uap={uap}&uapv=15.0.0&uaw=0&are=1&pae=1&frm=0&pscdl=noapi&_eu=EEA&_s=2&sid={sid}&sct=1&seg=1&dl={uri_dl}&dt={uri_dt}&en=stake&_ee=1&tfd={tfd1}&_z=fetch"

    return {
        'tracker': tracker


    }


# === Device settings ===
devices = [
    {"name": "iPhone X", "width": 375, "height": 812, "mobile": True},
    {"name": "Pixel 2", "width": 411, "height": 731, "mobile": True},
    {"name": "iPad", "width": 768, "height": 1024, "mobile": True},
]


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}

while True:
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
            url = "https://gamemoney.in/?utm_source=AdReliant&utm_medium=cpm"

            driver.get(str(url))
            print('wait for 2 seconds')
            time.sleep(2)
            url = generate_urls()
            requests.get(url=url['tracker'], headers=header)
            driver.quit()

        except Exception as e:
            pass

    # Optional delay between full cycles, e.g., 60 seconds
    print("Cycle complete, waiting 5 seconds before next run...")
    time.sleep(5)
