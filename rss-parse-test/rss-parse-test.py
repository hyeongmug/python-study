import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=3014000000')
doc = res.text
xml=BeautifulSoup(doc)
result = xml.findAll('wfkor')
resultLength = len(result)

for item in result:
    print(item.text)