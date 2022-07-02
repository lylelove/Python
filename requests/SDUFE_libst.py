import requests

hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/99.0.4844.82 Safari/537.36','Referer':'http://libst.sdufe.edu.cn/home/web/index'}
url="http://libst.sdufe.edu.cn/home/web/f_second"
cookies="userid=20190611509; user_name=%E5%88%98%E8%80%98%E9%BA%9F; access_token=afc504d9bccba86451816be61d2817e1; "
r= requests.Session()
r.cookies['cookies']=cookies
response = r.get(url,headers=hd)
cookies = r.cookies
a = cookies.get_dict()
print(response.text)