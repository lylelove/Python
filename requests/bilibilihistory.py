import requests
import time

cookies="_uuid=FB5B91B7-310AA-DC35-10B10B-6ED3951BECCE85397infoc; SESSDATA=f4d7ca06%2C1672479765%2Cfabf8*71"
url="https://api.bilibili.com/x/web-interface/history/cursor"
hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/99.0.4844.82 Safari/537.36'}
r= requests.Session()
r.cookies['cookies']=cookies
response = r.get(url,headers=hd)
h_list=response.json()['data']['list']
h_num=len(h_list)
h_time=0
h_tags=[]
h_author_name=[]
watch_time=0
for i in range(len(h_list)):
    if h_list[i]['progress'] == -1:
        watch_time = watch_time + h_list[i]['duration']
    else:
        watch_time = watch_time + h_list[i]['progress']
while len(h_list)>0:
    h_time = h_list[len(h_list)-1]['view_at']
    url = "https://api.bilibili.com/x/web-interface/history/cursor?view_at="+str(h_time)
    response = r.get(url,headers=hd)
    h_list = response.json()['data']['list']
    h_num=h_num+ len(h_list)
    for i in range(len(h_list)):
        h_tags.append(h_list[i]['tag_name'])
        h_author_name.append(h_list[i]['author_name'])
        if h_list[i]['progress']==-1:
            watch_time=watch_time+h_list[i]['duration']
        else:
            watch_time = watch_time + h_list[i]['progress']
    print("已查询到"+str(h_num)+"条记录")
h_time=time.localtime(h_time)
print("最早可查询记录为："+time.strftime("%Y-%m-%d %H:%M:%S", h_time))
watch_time=watch_time/60
print("总计观看"+str(watch_time)+"分钟")
tag_names=list(set(h_tags))
tag_names.pop(0)
tag_names_num=[]
for i in range(len(tag_names)):
    tag_names_num.append(h_tags.count(tag_names[i]))
author_name = list(set(h_author_name))
author_name.pop(0)
author_name_num=[]
for i in range(len(author_name)):
    author_name_num.append(h_author_name.count(author_name[i]))
print("观看次数前五名如下：")
print("标签：")
for i in range(5):
    max_num=tag_names_num.index(max(tag_names_num))
    max_watch_tag=tag_names[max_num]
    max_watch_tag_num=tag_names_num[max_num]
    tag_names.pop(max_num)
    tag_names_num.pop(max_num)
    print("tag："+max_watch_tag+"，观看次数："+str(max_watch_tag_num)+"次")
print("up主：")
for i in range(5):
    max_num=author_name_num.index(max(author_name_num))
    max_watch_up=author_name[max_num]
    max_watch_up_num=author_name_num[max_num]
    author_name.pop(max_num)
    author_name_num.pop(max_num)
    print("up："+max_watch_up+"，观看次数："+str(max_watch_up_num)+"次")

