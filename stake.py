# -*- coding: utf-8 -*-
import time
import random
import urllib.parse
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# === Google Analytics tracker config ===
tid = "G-WMCTNCHSPP"
gtm = "45je4cc1v9108524162za200"
gcd = "13l3l3l3l1l1"
dl = 'https://adreliant.com/'
dt = "RECRD"
total_minute = 1.25
average_session_duration = 60

# === Tracker configuration ===
value = 1000 * 60
ir = '1'
isMobile = True
isDesktop = False
baseUrl = 'https://analytics.google.com/g/collect?'
version = '2'
npa = '0'
dma = '0'
tag_exp = '0'
ul = 'en-us'
dr = ''
uri_dr = urllib.parse.quote(dr)

sr_mobile_arr = ['360×800']
uam_arr = ['SM-G955U']

uaa_desktop_arr = ["x86"]
uab_desktop_arr = ['32', '64']
userAgentMapping = {
    "Chromium OS": "Not%2FA)Brand;8.0.0.0|Chromium;126.0.6478.128|Google%20Chrome;126.0.6478.128",
}
sr_desktop_arr = ['1366x768']


def generate_urls():
    sid = int(time.time())
    cid = f"{100000000 + random.randint(0, 1) + random.randint(0, 100000000)}.{sid}"
    p = random.randint(0, 2147483647)
    tfd1 = 100 + random.randint(0, 4000)
    tfd2 = tfd1 + random.randint(0, 400)
    et = total_minute * value + random.randint(0, 9999)

    uab = uamb = uap = uam = uafvl = sr = uaa = ''

    if isMobile:
        sr = random.choice(sr_mobile_arr)
        uap = 'Android'
        uamb = '1'
        uam = urllib.parse.quote(random.choice(uam_arr))
    elif isDesktop:
        sr = random.choice(sr_desktop_arr)
        uab = random.choice(uab_desktop_arr)
        uamb = '0'
        uaa = random.choice(uaa_desktop_arr)
        uam = ''
        rand_key = random.choice(list(userAgentMapping.keys()))
        uap = urllib.parse.quote(rand_key)
        uafvl = urllib.parse.quote(userAgentMapping[rand_key])

    return {
        'tracker': f"{baseUrl}v={version}&tid=G-WZXPX61NKF&gtm={gtm}&_p={p}&gcd={gcd}&npa={npa}&dma={dma}&tag_exp={tag_exp}"
                   f"&cid={cid}&ul={ul}&sr={sr}&ir={ir}&uaa={uaa}&uab={uab}&uafvl={uafvl}&uamb={uamb}&uam={uam}&uap={uap}"
                   f"&uapv=15.0.0&uaw=0&are=1&pae=1&frm=0&pscdl=noapi&_eu=EEA&_s=2&sid={sid}&sct=1&seg=1"
                   f"&dl={urllib.parse.quote(dl)}&dt={urllib.parse.quote(dt)}&en=Recrd&_ee=1&tfd={tfd1}&_z=fetch"
    }


def get_headers(is_mobile):
    user_agent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
        if is_mobile else
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    )
    return {
        "User-Agent": user_agent,
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }


# === Device settings ===
devices = [
    {"name": "iPhone X", "width": 375, "height": 812, "mobile": True},
    {"name": "Pixel 2", "width": 411, "height": 731, "mobile": True},
    {"name": "iPad", "width": 768, "height": 1024, "mobile": True},
    {"name": "Desktop 1366x768", "width": 1366, "height": 768, "mobile": False},
    {"name": "Desktop 1920x1080", "width": 1920, "height": 1080, "mobile": False}
]

url = "https://adsonick.blogspot.com/2025/05/stakelink4.html"

# === Main loop ===
for device in devices:
    print(f"Opening as {device['name']}")
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--headless=new")
    options.binary_location = "/usr/bin/google-chrome"

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
        # path = 'C:\WebDriver\bin\chromedriver.exe'
        path = "/usr/bin/chromedriver"
        service = Service()
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)

        urls = generate_urls()
        requests.get(urls['tracker'], headers=get_headers(device['mobile']))
        time.sleep(4)
        driver.quit()

    except Exception as e:
        print(f"Error: {e}")
        os._exit(1)
