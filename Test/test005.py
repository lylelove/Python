import re

import requests

hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/99.0.4844.82 Safari/537.36'}
buildings = []
places = []
addresses = []
prices = []
images = []
for i in range(1, 5):
    url = 'https://www.zhifang.com/project/03sd100000000000000_' + str(i) + '.html'
    response = requests.get(url, headers=hd)
    info = response.text
    pat_buildings = r'<h4><a href="/project\d+/" target="_blank">(.*?)</a></h4>'
    pat_places = r'<p class="margin_top10">区域：<a href="/project/\w+.html">(.*?)</a>-<a href="/project/\w+.html">(' \
                 r'.*?)</a>-<a href="/project/\w+.html">(.*?)</a></p> '
    pat_addresses = r'<p>地址：(.*?)</p>'
    pat_prices = r'<div class="price">.*?<strong>(.*?)</strong>.*?</div>'
    pat_images = r'<a href="/project\d+/" target="_blank"><img src="(.*?)"'
    buildings = buildings + re.compile(pat_buildings, re.S).findall(info)
    places = places + re.compile(pat_places, re.S).findall(info)
    addresses = addresses + re.compile(pat_addresses, re.S).findall(info)
    prices = prices + re.compile(pat_prices, re.S).findall(info)
    images = images + re.compile(pat_images, re.S).findall(info)
print(images)