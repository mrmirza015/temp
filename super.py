# -*- coding: utf-8 -*-
import requests
import random
import string
import urllib.parse
import time
import json
import re
import threading
import json
import brotli
import gzip


# here
tid = "G-WMCTNCHSPP"
gtm = "45je4cc1v9108524162za200"
gcd = "13l3l3l3l1l1"
dl = 'https://example.com/'
dt = "stake"
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
    '360×800',
]
uam_arr = [
    'SM-G955U']


# Desktop Configurations
uaa_desktop_arr = [
    "x86"
]


uab_desktop_arr = ['32', '64']

userAgentMapping = {
    "Chromium OS": "Not%2FA)Brand;8.0.0.0|Chromium;126.0.6478.128|Google%20Chrome;126.0.6478.128",

}


sr_desktop_arr = [
    '1366x768',
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

    tracker = f"{baseUrl}v={version}&tid=G-WZXPX61NKF&gtm={gtm}&_p={p}&gcd={gcd}&npa={npa}&dma={dma}&tag_exp={tag_exp}&cid={cid}&ul={ul}&sr={sr}&ir={ir}&uaa={uaa}&uab={uab}&uafvl={uafvl}&uamb={uamb}&uam={uam}&uap={uap}&uapv=15.0.0&uaw=0&are=1&pae=1&frm=0&pscdl=noapi&_eu=EEA&_s=2&sid={sid}&sct=1&seg=1&dl={uri_dl}&dt={uri_dt}&en=stake_fv&_ee=1&tfd={tfd1}&_z=fetch"

    return {

        'tracker': tracker


    }


# here


def extract_selected_fields(response):
    match = re.search(r'\{.*\}', response)
    if not match:
        raise ValueError("JSON object not found in response")

    user_data = json.loads(match.group())

    return {
        's': user_data.get('s'),
        'e': user_data.get('e'),
        'bv': user_data.get('bv'),
        'r': user_data.get('r'),
    }


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


def should_trigger(x):
    return random.random() < (float(x)/100)


def get_unix_timestamp():
    return int(time.time())


def get_random_resolution(isMobile: bool):
    if isMobile:
        mobile_resolutions = [
            (360, 640), (375, 667), (414, 896), (390, 844),
            (412, 915), (360, 780), (428, 926), (393, 873)
        ]
        width, height = random.choice(mobile_resolutions)
    else:
        desktop_resolutions = [
            (1366, 768), (1440, 900), (1536, 864), (1600, 900),
            (1920, 1080), (1280, 720), (1680, 1050), (2560, 1440)
        ]
        width, height = random.choice(desktop_resolutions)

    resolution_str = f"{width}x{height}"
    return resolution_str, width, height


def generate_n_digit_number(n: int) -> int:
    if n <= 0:
        raise ValueError("Number of digits must be positive.")
    start = 10**(n - 1)
    end = 10**n - 1
    return random.randint(start, end)


def generate_uuid_v4():
    # Generate 16 random bytes
    random_bytes = [random.randint(0, 255) for _ in range(16)]
    # Set version (4) and variant (10)
    random_bytes[6] = (random_bytes[6] & 0x0F) | 0x40  # version 4
    random_bytes[8] = (random_bytes[8] & 0x3F) | 0x80  # variant 10

    # Convert bytes to hex and format as UUID
    hex_bytes = [f"{b:02x}" for b in random_bytes]
    uuid_str = (
        f"{''.join(hex_bytes[0:4])}-"
        f"{''.join(hex_bytes[4:6])}-"
        f"{''.join(hex_bytes[6:8])}-"
        f"{''.join(hex_bytes[8:10])}-"
        f"{''.join(hex_bytes[10:16])}"
    )
    return uuid_str


def get_unix_time_millis_float():
    t = time.time()
    millis = int(t * 1000)
    frac = t * 1000 - millis
    return float(f"{millis}{str(frac)[1:]}")


def get_urls(s, e, bv, r, isMobile):
    t = get_unix_timestamp()
    id = '1612409'
    m = '0'
    p = 'V2luMTA'
    os = 'Win10'
    res_str, w, h = get_random_resolution(isMobile=isMobile)
    mob = '0'
    ruri = 'aHR0cHM6Ly9hZHNvbmljay5ibG9nc3BvdC5jb20v'
    uuid = generate_uuid_v4()
    if isMobile:
        id = '1612410'
        m = '1'
        p = 'QW5kcm9pZA'
        os = 'Android'
        mob = '1'

    ping2 = f"https://sender.cleverwebserver.com/group/93000?id={id}&ref=aHR0cHM6Ly9nYW1lbW9uZXkuaW4vP3V0bV9zb3VyY2U9QWRSZWxpYW50JnV0bV9tZWRpdW09Y3Bt&ruri={ruri}&t={t}&cmpId=&fb=0&wl=1&furl=0&sf=0&bw=Q2hyb21l&b=0&m={m}&p={p}&res={res_str}&app=&v=2.39.5&s={s}&e={e}&bv={bv}&cont=AS&st=W&sdk=&mng=&lg=en-US&iv=-1&ctr=IN&sz={h}&landing=1&hei={w}.00px&ts=0.{generate_n_digit_number(3)}"

    ping3 = f"https://call.cleverwebserver.com/?id=93000&c=IN&r={r}&l={generate_n_digit_number(3)}&b=Chrome&bv={bv}&os={os}&mob={mob}&v=2.39.5&lg=en-US&ref=aHR0cHM6Ly9nYW1lbW9uZXkuaW4vP3V0bV9zb3VyY2U9QWRSZWxpYW50JnV0bV9tZWRpdW09Y3Bt&ruri={ruri}&s={s}&e={e}&st=W&iv=-1"

    payload1 = {
        "dt": "",
        "eventType": 1,
        "firstContentfulPaint": 0,
        "firstPaint": generate_n_digit_number(4),
        "location": "https://c.clvrads.com/creative_files/YmYwNmExZjIwYTI/widescreensponsor/",
        "memory": {
            "totalJSHeapSize": 3853004,
            "usedJSHeapSize": 2175728,
            "jsHeapSizeLimit": 2248146944
        },
        "nt": "navigate",
        "pageloadId": uuid,
        "referrer": "https://gamemoney.in/",
        "resources": [],
        "serverTimings": [
            {
                "name": "cfCacheStatus",
                "dur": 0,
                "desc": "DYNAMIC"
            }
        ],
        "siteToken": "483f71c38243406b9c2100ac484fdce0",
        "st": 2,
        "startTime": get_unix_time_millis_float(),
        "timingsV2": {
            "unloadEventStart": 0,
            "unloadEventEnd": 0,
            "domInteractive": f'{generate_n_digit_number(4)}.{generate_n_digit_number(13)}',
            "connectEnd": f'{generate_n_digit_number(3)}.{generate_n_digit_number(13)}',
            "connectStart": generate_n_digit_number(3),
            "criticalCHRestart": 0,
            "decodedBodySize": generate_n_digit_number(5),
            "deliveryType": "",
            "domComplete": f'{generate_n_digit_number(4)}.{generate_n_digit_number(13)}',
            "domContentLoadedEventEnd": f'{generate_n_digit_number(4)}.{generate_n_digit_number(13)}',
            "domContentLoadedEventStart": f'{generate_n_digit_number(4)}.{generate_n_digit_number(13)}',
            "domainLookupEnd": generate_n_digit_number(3),
            "domainLookupStart": f'{generate_n_digit_number(3)}.{generate_n_digit_number(13)}',
            "duration": f'{generate_n_digit_number(4)}.{generate_n_digit_number(13)}',
            "encodedBodySize": random.randint(3600, 3620),
            "entryType": "navigation",
            "fetchStart": f'{generate_n_digit_number(3)}.{generate_n_digit_number(13)}',
            "finalResponseHeadersStart": f'{generate_n_digit_number(4)}.{generate_n_digit_number(13)}',
            "firstInterimResponseStart": 0,
            "initiatorType": "navigation",
            "loadEventEnd": f'{generate_n_digit_number(4)}.{generate_n_digit_number(13)}',
            "loadEventStart": f'{generate_n_digit_number(4)}.{generate_n_digit_number(13)}',
            "name": "https://c.clvrads.com/creative_files/YmYwNmExZjIwYTI/widescreensponsor/?tracker=aHR0cHM6Ly9zdGFrZS5iZXQvP2M9QkJDUEEzODk3NTI3SkZG",
            "nextHopProtocol": "h2",
            "redirectCount": 0,
            "redirectEnd": 0,
            "redirectStart": 0,
            "renderBlockingStatus": "non-blocking",
            "requestStart": f'{generate_n_digit_number(3)}.{generate_n_digit_number(13)}',
            "responseEnd": f'{generate_n_digit_number(3)}.{generate_n_digit_number(13)}',
            "responseStart": f'{generate_n_digit_number(3)}.{generate_n_digit_number(13)}',
            "responseStatus": 200,
            "secureConnectionStart": f'{generate_n_digit_number(3)}.{generate_n_digit_number(13)}',
            "startTime": 0,
            "transferSize": random.randint(3900, 3920),
            "type": "navigate",
            "unloadEventEnd": 0,
            "unloadEventStart": 0,
            "workerStart": 0
        },
        "versions": {
            "fl": "2025.4.0-1-g37f21b1",
            "js": "2024.6.1",
            "timings": 2
        }
    }

    payload2 = {
        "dt": "",
        "eventType": 3,
        "cls": {
            "value": 0,
            "path": "/creative_files/YmYwNmExZjIwYTI/widescreensponsor/"
        },
        "fcp": {
            "value": random.randint(1250, 1850),
            "path": "/creative_files/YmYwNmExZjIwYTI/widescreensponsor/"
        },
        "fid": {
            "value": -1
        },
        "inp": {
            "value": -1
        },
        "landingPath": "/creative_files/YmYwNmExZjIwYTI/widescreensponsor/",
        "lcp": {
            "value": random.randint(1250, 1850),
            "path": "/creative_files/YmYwNmExZjIwYTI/widescreensponsor/",
            "element": "#img_1097615",
            "it": "img"
        },
        "erd": f'{generate_n_digit_number(3)}.{generate_n_digit_number(13)}',
        "fp": None,
        "it": "img",
        "path": "/creative_files/YmYwNmExZjIwYTI/widescreensponsor/",
        "rld": f'{generate_n_digit_number(3)}.{generate_n_digit_number(13)}',
        "rlt": f'{generate_n_digit_number(2)}.{generate_n_digit_number(13)}',
        "size": random.randint(4250, 4850),
        "url": "https://c.clvrads.com/creative_files/YmYwNmExZjIwYTI/widescreensponsor/images/3cdcc48ef837ffe686db9a652c82ece4.svg",
        "value": random.randint(1250, 1850),
        "location": "https://c.clvrads.com/creative_files/YmYwNmExZjIwYTI/widescreensponsor/",
        "nt": "navigate",
        "pageloadId": uuid,
        "referrer": "https://gamemoney.in/",
        "serverTimings": [
            {
                "name": "cfCacheStatus",
                "dur": 0,
                "desc": "DYNAMIC"
            }
        ],
        "siteToken": "483f71c38243406b9c2100ac484fdce0",
        "st": 1,
        "startTime": get_unix_time_millis_float(),
        "timingsV2": {
            "nextHopProtocol": "h2",
            "transferSize": random.randint(3250, 3850),
            "decodedBodySize": random.randint(15250, 16850)
        },
        "ttfb": {
            "value":  f'{generate_n_digit_number(2)}.{generate_n_digit_number(13)}',
            "path": "/creative_files/YmYwNmExZjIwYTI/widescreensponsor/"
        },
        "versions": {
            "js": "2024.6.1",
            "fl": "2025.4.0-1-g37f21b1"
        }
    }
    ping4 = f'https://c.clvrads.com/creative_files/YmYwNmExZjIwYTI/widescreensponsor/?tracker=aHR0cHM6Ly9zdGFrZS5iZXQvP2M9QkJDUE8zODk3NTI3SkZG'

    return {
        "ping2": ping2,
        "ping3": ping3,
        'ping4': ping4,
        'payload1': payload1,
        'payload2': payload2
    }


ping1 = "https://ui.cleverwebserver.com/"


def getProxy():
    user = ["spbxg3myys"]
    key = ['Gb1u5yZ=8lthp9QQps']
    cities = ["mumbai", "chennai", "kolkata",
              "bengaluru", "pune", "hyderabad", "ahmedabad"]

    index = random.randint(0, len(user) - 1)
    username = f'user-{user[index]}-country-IN'
    # print(username)
    password = key[index]
    proxy = f"http://{username}:{password}@gate.decodo.com:7000"
    proxies = {
        'http': proxy,
        'https': proxy
    }
    return proxies


session = requests.Session()
# session.proxies = getProxy()
session.headers.update({'Connection': 'keep-alive'})


def request(url, headers=None, proxies=None):

    if headers is None:
        headers = session.headers
    if proxies is None:
        proxies = session.proxies

    try:

        response = session.get(url, headers=headers, proxies=proxies)

        print(response.status_code, url)
        print('\n')
        return response
    except requests.exceptions.RequestException as error:
        print('Error:', error)
        print('\n')
        return None


def get_random_user_agent(is_mobile: bool) -> str:
    mobile_agents = [
        "Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
    ]

    desktop_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    ]

    return random.choice(mobile_agents if is_mobile else desktop_agents)


def get_headers_ss(is_mobile: bool) -> dict:
    if is_mobile:
        return {
            "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "priority": "i",
            "referer": "https://gamemoney.in/",
            "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "sec-fetch-dest": "image",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "cross-site",
            "sec-fetch-storage-access": "active",
            "user-agent": get_random_user_agent(True)
        }
    else:
        return {
            "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
            "priority": "i",
            "referer": "https://gamemoney.in/",
            "sec-ch-ua": '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "image",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "cross-site",
            "sec-fetch-storage-access": "none",
            "user-agent": get_random_user_agent(False)
        }


rum = 'https://c.clvrads.com/cdn-cgi/rum?'


def start_requests(iterations):
    def make_requests():
        isMobile = should_trigger(50)
        headers = get_headers(is_mobile=isMobile)
        headers_ss = get_headers_ss(is_mobile=isMobile)
        # print(headers_ss)
        response1 = request(ping1, headers=headers)
        content = response1.text
        print(content)
        encoding = response1.headers.get("Content-Encoding", "")
        if encoding == "br":
            content = brotli.decompress(response1.content)
        elif encoding == "gzip":
            content = gzip.decompress(response.content)
        else:
            content = response.content

        text = content.decode("utf-8", errors="replace")
        print(text[:1000])

        fields = extract_selected_fields(str(content))
        # print(response)
        urls = get_urls(s=fields['s'], e=fields['e'],
                        bv=fields['bv'], r=fields['r'], isMobile=isMobile)
        # print(json.dumps(urls['payload1'], indent=2))
        # print(json.dumps(urls['payload2'], indent=2))
        response2 = request(urls['ping2'], headers)
        response3 = request(urls['ping3'], headers_ss)
        response4 = request(urls['ping4'], headers)
        payload1 = urls['payload1'],
        payload2 = urls['payload2']
        response5 = requests.post(rum, json=payload1, headers=headers)
        response6 = requests.post(rum, json=payload2, headers=headers)
        print(response5.status_code)
        print(response6.status_code)
        ga_url = generate_urls()
        if response1.status_code == 200 and response2.status_code == 200 and response3.status_code == 200 and response5.status_code == 200 and response6.status_code == 200 and response4.status_code == 200:
            request(ga_url['tracker'], headers=headers)

    for i in range(iterations):
        threading.Timer(i * 2, make_requests).start()


start_requests(1)

