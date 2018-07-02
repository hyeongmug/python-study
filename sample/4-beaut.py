from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <div id="meigen">
                <h1>위키북스 도서</h1>
                <ul class="items">
                    <li>유니티 게임 이펙트 입문</li>
                    <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
                    <li>모던 웹사이트 디자인의 정석</li>'
                </ul>
            </div>
        </body>
    </html>
"""

soup = BeautifulSoup(html, 'html.parser')

header = soup.select_one("body > div > h1") # 요소
list_items = soup.select("ul.items > li") # 요소의 배열

print(header.string)
# soup.select_one('ul').attrs['class]
print(soup.select_one('ul').attrs)
for li in list_items:
    print(li.string)