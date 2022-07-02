import re
import base64
import ddddocr
import requests

hd = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'Referer': 'http://card.sdufe.edu.cn/Page/Page', 'Origin': 'http://card.sdufe.edu.cn', 'Connection': 'keep-alive',
    'Host': 'card.sdufe.edu.cn', 'Accept': 'application/json, text/javascript, */*; q=0.01', }
cookies = "username=20190611509;hallticket=891868E4656849DC9DF9FF134F7A5B2B"
number = '20190611509'
password = '263232'

def get_cookies(hd):
    url = "http://card.sdufe.edu.cn/"
    with requests.Session() as s:
        r = s.post(url, headers=hd)
        cookies = r.cookies
        a = cookies.get_dict()
    return a


def get_img(cookies):
    imagetest = requests.get('http://card.sdufe.edu.cn/Login/GetValidateCode', cookies=cookies)
    imagebody = imagetest.content
    file_name = 'index.png'
    with open(file_name, "wb") as f:
        f.write(imagebody)


def get_verify():
    try:
        ocr = ddddocr.DdddOcr()
        with open("index.png", 'rb') as f:
            img_bytes = f.read()
        verify = ocr.classification(img_bytes)
    except:
        verify = 0000
    return verify


def get_login(cookies,hd,number,password):
    pw = bytes(password,'UTF-8')
    pw = base64.b64encode(pw)
    pw = str(pw)
    pat_pw=r"b\'(.*?)\'"
    pw = re.compile(pat_pw, re.S).findall(pw)
    loopcount = 0
    logincode = 201
    loginurl = 'http://card.sdufe.edu.cn/Login/LoginBySnoQuery'
    while logincode == 201:
    # try:
        get_img(cookies)
        verify = get_verify()
        print(verify)
        r = requests.Session()
        # r.cookies['cookies'] = cookies
        data = {'sno':str(number),'pwd':pw[0],'ValiCode':str(verify),'remember':'1','uclass':'1s','json':'true'}
        response = r.post(url=loginurl, headers=hd, data=data,cookies=cookies)
        logincode = response.json()['code']
        cookies = r.cookies
        a = cookies.get_dict()
        return a
    # # except:
    #         logincode = 201
    #     loopcount += 1
        print('{} is {}'.format(loopcount, logincode))

    print('finish login...')


def get_date(cookies, hd):
    url = "http://card.sdufe.edu.cn/Report/GetPersonTrjn"
    r = requests.Session()
    r.cookies['cookies'] = cookies
    response = r.post('http://card.sdufe.edu.cn/User/GetCardInfoByAccountNoParm', headers=hd)
    msg = response.json()['Msg']
    pat_account = r'{ "account":"(.*?)", "name":'
    account = re.compile(pat_account, re.S).findall(msg)
    params = {'sdate': '2019-01-01', 'edate': '2022-04-11', 'account': account[0], 'page': '1', 'rows': '20000'}
    response = r.post(url, headers=hd, data=params)
    data = response.json()
    cost_list = data['rows']
    cost_num = 0
    cost_s = 0
    cost_place = []
    for i in range(len(cost_list)):
        if cost_list[i]['TRANAMT'] < 0:
            cost_num = cost_num + abs(cost_list[i]['TRANAMT'])
            cost_s = cost_s + 1
            cost_place.append(cost_list[i]['MERCNAME'])
    cost_place_names = list(set(cost_place))
    cost_place_names.pop(cost_place_names.index(''))
    cost_place_sum = []
    for i in range(len(cost_place_names)):
        c_time = 0
        c_sum = 0
        temp = []
        for j in range(len(cost_list)):
            if cost_list[j]['MERCNAME'] == cost_place_names[i]:
                c_time = c_time + 1
                c_sum = c_sum + abs(cost_list[j]['TRANAMT'])
        temp.append(cost_place_names[i].rstrip())
        temp.append(int(c_time))
        temp.append(int(c_sum))
        temp.append(round((int(c_sum) / int(c_time)), 2))
        cost_place_sum.append(temp)

    for i in range(len(cost_place_sum)):
        for j in range(len(cost_place_sum)):
            if cost_place_sum[j][2] < cost_place_sum[i][2]:
                temp = cost_place_sum[j]
                cost_place_sum[j] = cost_place_sum[i]
                cost_place_sum[i] = temp

    print("从2019年到今天花了" + str(round(cost_num, 2)) + "元")
    for i in range(len(cost_place_sum)):
        print(
            cost_place_sum[i][0] + "，次数：" + str(cost_place_sum[i][1]) + "，花费：" + str(
                cost_place_sum[i][2]) + "，平均每次：" + str(
                cost_place_sum[i][3]))


print(get_login(get_cookies(hd),hd,number,password))
