import re
import requests

# 完成爬取智房网楼盘名称，楼盘区域，楼盘地址和楼盘价格信息。
# 网址：https://www.zhifang.com/project/03sd100010300000000.html

hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/99.0.4844.82 Safari/537.36'}
b_names = []
b_addresses = []
b_prices = []
url = 'https://www.zhifang.com/project/03sd100010300000000.html'
response = requests.get(url, headers=hd)
info = response.text
pattern = re.compile(r'\s+')
info=re.sub(pattern,'', info)
pat_b_name = r'<divclass="name"><ahref="https://www.zhifang.com/project\d+/"target="_blank">(.*?)</a>'
pat_b_address=r'<divclass="location"><i></i><ahref="https://www.zhifang.com/project/\w+.html"targe="_blank">(.*?)</a><span>-</span><ahref="https://www.zhifang.com/project/\w+.html"targe="_blank">(.*?)</a><span>-</span><ahref="https://www.zhifang.com/project/\w+.html"targe="_blank">(.*?)</a><p>(.*?)</p></div>'
pat_b_price=r'<divclass="price"><strong>(.*?)</strong>'
b_names = b_names + re.compile(pat_b_name, re.S).findall(info)
b_addresses = b_addresses + re.compile(pat_b_address, re.S).findall(info)
b_prices = b_prices + re.compile(pat_b_price, re.S).findall(info)