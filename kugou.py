import requests
from bs4 import BeautifulSoup
import json

# 1. 构造请求URL
base_url = "https://www.kugou.com/mixsong/gs0pc0f.html?fromsearch=收敛水"

 # 2. 设置请求头，模拟浏览器访问
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

# 3. 发送HTTP请求
response = requests.get(base_url, headers=headers)
response.raise_for_status()  # 检查请求是否成功
response.encoding = 'utf-8'  # 设置编码

# 4. 解析HTML页面
soup = BeautifulSoup(response.text, 'html.parser')
# 5. 提取歌曲信息

# 提取歌曲名称
song_name_tag = soup.find('span', class_='audioName')
print("歌曲:"+song_name_tag.string)


# 提取歌手名字
singer_name=soup.find_all("p", class_='singerName fl')
for singerNamefl in singer_name:
    all_name=singerNamefl.find_all("a")
    for name in all_name:
        print("歌手："+name.string)


     # 提取专辑信息
    clumb_name = soup.find_all("p", class_="albumName fl")
    for albumNamefl in clumb_name:
        al_name = albumNamefl.find_all("a")
        for name1 in al_name:
            print("专辑："+name1.string)

