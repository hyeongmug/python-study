import requests
from bs4 import BeautifulSoup

session = requests.session()
request = session.get("http://naver.com")
html = request.text

soup = BeautifulSoup(html, 'html.parser')
text = soup.select('.plus_txt')[0].text

print(text)
