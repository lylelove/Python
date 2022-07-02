import requests
import re
import markdown

hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/99.0.4844.82 Safari/537.36'}
url="https://api.github.com/repos/lylelove/lylelove.github.io/issues?PRIVATE-TOKEN=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"

response = requests.get(url, headers=hd)

data=response.json()
bodys=[]
titles=[]
briefings=[]
for issue in data:
    bodys.append(markdown.markdown(re.sub(r'\r\n','\r\n\r\n',issue['body'])))
    titles.append(issue['title'])
    briefings.append(markdown.markdown(re.search(r'.*?\r\n',issue['body'],re.M|re.I).group()))

