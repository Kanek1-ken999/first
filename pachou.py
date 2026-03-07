from bs4 import BeautifulSoup
#引入beautiful Soup库
import requests
#引入Python requests库
headers= {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0"
}
#定义请求头，使用User_Agent包装程序为浏览器，防止被防爬虫程序阻隔
for start_num in range(0,250,25):
    #使用 for循环保证前250名影片名字全部覆盖
 response=requests.get(f"https://movie.douban.com/top250?start={start_num}",headers=headers)
    #引入要爬取的网址，以及开始和结束的元素索引值
 abc=response.text
 soup = BeautifulSoup(abc,"html.parser")
 titles = soup.find_all("span",attrs={"class":"title"})#attrs作用是根据元素属性提取内容
 for title in titles:
     #使用for循环筛选中文电影名
    t=title.string
    if "/" not in t:
          print(t)



