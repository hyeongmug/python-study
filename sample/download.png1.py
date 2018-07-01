import urllib.request

url = "http://uta.pw/shodou/img/28/214.png"
savename = "test.png"

# 다운로드
men = urllib.request.urlopen(url).read()

with open(savename, mode="wb") as f:
    f.write(men)
    print("저장되었습니다.")

# urllib.request.urlretrieve(url, savename)