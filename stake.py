import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

# here

import requests
import random
import string
import urllib.parse
import time
import json
import re
import threading
import json

import json
import re


# here
tid = "G-WMCTNCHSPP"
gtm = "45je4cc1v9108524162za200"
gcd = "13l3l3l3l1l1"
dl = 'https://adreliant.com/'
dt = "RECRD"
total_minute = 1.25
average_session_duration = 60
# common configuration
baseUrl = 'https://analytics.google.com/g/collect?'
version = '2'
npa = '0'
dma = '0'
tag_exp = '0'
ul = 'en-us'
dr = ''
uri_dr = dr
value = 1000 * 60
ir = '1'
isMobile = True
isDesktop = False
sr_mobile_arr = [
    '360×800', '414×896', '360×640', '412×915', '390×844',
    '360×780', '375×667', '375×812', '360×760', '393×851',
    '393×873', '412×892', '428×926', '360×720', '385×854',
    '412×869', '414×736', '412×846', '360×740', '384×854'
]
uam_arr = [
    'SM-G955U', 'SM-G981B', 'SM-F946U', 'SM-A715F', 'SM-G780F',
    'SM-G985U', 'SM-N975F', 'SM-A515F', 'SM-G770F', 'SM-M315F',
    'Pixel 6', 'Pixel 6 Pro', 'Pixel 5', 'Pixel 4a', 'Pixel 4',
    'Pixel 3 XL', 'OnePlus 9', 'OnePlus 9 Pro', 'OnePlus 8T',
    'OnePlus 8', 'OnePlus Nord', 'OnePlus 7T', 'Redmi Note 11',
    'Mi 11', 'Mi 11 Ultra', 'Redmi Note 10 Pro', 'Poco X3 Pro',
    'Redmi K40', 'Find X3 Pro', 'Reno 6 Pro', 'A94 5G', 'Reno 5 Pro',
    'Find X2', 'Reno 4 Pro', 'Moto G Power 2021', 'Moto G Stylus 2021',
    'Edge 20', 'Edge 20 Pro', 'Moto G100', 'Moto E 2020', 'Xperia 1 III',
    'Xperia 5 III', 'Xperia 10 III', 'Xperia 1 II', 'Xperia 5 II', 'Xperia 10 II', 'iPhone 15 Plus', 'iPhone 15 Pro Max', 'iPhone 14 Plus', 'iPhone 14 Pro', 'iPhone 14 Pro Max', 'iPhone 13', 'iPhone 13 Pro', 'iPhone 13 Pro Max', 'iPhone 12', 'iPhone 12 Mini', 'iPhone 12 Pro', 'iPhone 11', 'iPhone 11 Pro', 'iPhone 11 Pro Max', 'iPhone SE (3rd Gen)', 'iPhone SE (2nd Gen)', 'iPhone XR', 'iPhone XS', 'iPhone XS Max']


# Desktop Configurations
uaa_desktop_arr = [
    "x86", "x86_64", "arm", "arm64", "mips", "mips64", "ppc",
    "ppc64", "sparc", "sparc64", "ia64", "riscv", "riscv64",
    "s390", "s390x"
]


uab_desktop_arr = ['32', '64']

userAgentMapping = {
    "Chromium OS": "Not%2FA)Brand;8.0.0.0|Chromium;126.0.6478.128|Google%20Chrome;126.0.6478.128",

}


sr_desktop_arr = [
    '1366x768', '1920x1080', '2560x1440', '3840x2160', '1280x800',
    '1600x900', '2560x1600', '2880x1800', '3200x1800', '3840x2400',
    '1920x1080', '2560x1440', '3840x2160', '5120x1440', '3840x1600',
    '7680x4320', '1600x1200', '2048x1152', '3440x1440', '2560x1080'
]


def get_current_minute():
    return 1000


def generate_urls():
    num = get_current_minute()
    uri_dl = urllib.parse.quote(dl)
    uri_dt = urllib.parse.quote(dt)
    uri_dr = urllib.parse.quote(dr)
    p = random.randint(0, 2147483647)
    sid = int(time.time())
    cid = f"{100000000 + random.randint(0, 1) + random.randint(0, 100000000)}.{sid}"
    et = total_minute * value + random.randint(0, 9999)
    tfd1 = 100 + random.randint(0, 4000)
    tfd2 = tfd1 + random.randint(0, 400)
    uab = ''
    uamb = ''
    uap = ''
    uam = ''
    uafvl = ''
    sr = ''
    uaa = ''

    if isMobile:
        sr = random.choice(sr_mobile_arr)
        uap = 'Android'
        uamb = '1'
        uam = urllib.parse.quote(random.choice(uam_arr))

    if isDesktop:
        sr = random.choice(sr_desktop_arr)
        uab = random.choice(uab_desktop_arr)
        uamb = '0'
        uam = ''
        uaa = random.choice(uaa_desktop_arr)
        random_key = random.choice(list(userAgentMapping.keys()))
        random_value = userAgentMapping[random_key]
        uap = urllib.parse.quote(random_key)
        uafvl = urllib.parse.quote(random_value)

    firstCall = f"{baseUrl}v={version}&tid={tid}&gtm={gtm}&_p={p}&gcd={gcd}&npa={npa}&dma={dma}&tag_exp={tag_exp}&cid={cid}&ul={ul}&sr={sr}&ir={ir}&uaa={uaa}&uab={uab}&uafvl={uafvl}&uamb={uamb}&uam={uam}&uap={uap}&uapv=15.0.0&uaw=0&are=1&pae=1&frm=0&pscdl=noapi&_eu=Ag&_s=1&sid={sid}&sct=1&seg=0&dl={uri_dl}&dt={uri_dt}&en=page_view&_fv=1&_ss=1&_ee=1&tfd={tfd1}&_z=fetch&ep.origin=firebase"

    tracker = f"{baseUrl}v={version}&tid=G-WZXPX61NKF&gtm={gtm}&_p={p}&gcd={gcd}&npa={npa}&dma={dma}&tag_exp={tag_exp}&cid={cid}&ul={ul}&sr={sr}&ir={ir}&uaa={uaa}&uab={uab}&uafvl={uafvl}&uamb={uamb}&uam={uam}&uap={uap}&uapv=15.0.0&uaw=0&are=1&pae=1&frm=0&pscdl=noapi&_eu=EEA&_s=2&sid={sid}&sct=1&seg=1&dl={uri_dl}&dt={uri_dt}&en=Recrd&_ee=1&tfd={tfd1}&_z=fetch"

    return {
        'firstCall': firstCall,

        'tracker': tracker


    }

# here


url = "https://adsonick.blogspot.com/2025/05/stakelink4.html"

# List of devices with screen sizes and mobile flag
devices = [
    {"name": "iPhone X", "width": 375, "height": 812, "mobile": True},
    {"name": "Pixel 2", "width": 411, "height": 731, "mobile": True},
    {"name": "iPad", "width": 768, "height": 1024, "mobile": True},
    {"name": "Desktop 1366x768", "width": 1366, "height": 768, "mobile": False},
    {"name": "Desktop 1920x1080", "width": 1920, "height": 1080, "mobile": False}
]


def get_headers(is_mobile):
    if is_mobile:
        user_agent = "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
        # print('mobile header')
    else:
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        # print('desktop header')

    headers = {
        "User-Agent": user_agent,
        "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }
    return headers


headers = get_headers(True)

for device in devices:
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-notifications")
    options.add_argument("--headless=new")

    if device["mobile"]:
        # Simulate mobile device
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
        # For desktop view
        options.add_argument(
            f"--window-size={device['width']},{device['height']}")

    print(f"Opening as {device['name']}")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        urls = generate_urls()
        requests.get(urls['tracker'], headers=headers)
        time.sleep(4)
    except:
        print('i am deleting this instance as error occured')
        os._exit(1)

    driver.quit()
