import feedparser as f

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

d = f.parse(url)

print(d['entries'][0]['wf'])
