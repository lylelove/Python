import requests
cookie=''
r = requests.Session()
r.cookies['cookies'] = cookies
data = {'sno': str(number), 'pwd': pw[0], 'ValiCode': str(verify), 'remember': '1', 'uclass': '1s', 'json': 'true'}
response = r.post(url=loginurl, headers=hd, data=data)
logincode = response.json()['code']
cookies = r.cookies
a = cookies.get_dict()