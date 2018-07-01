import urllib.request
url = "https://api.aoikujira.com/ip/ini"

men = urllib.request.urlopen(url).read()
print(men.decode("euc-kr"))