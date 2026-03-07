# 知网CNKI文献摘要爬虫程序

## 程序说明

## 完整代码
import requests
from bs4 import BeautifulSoup
import time
import random

# 目标网址
url = "https://example.com"  # 请替换为实际要爬取的网址

# 模拟浏览器请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    # 发送GET请求
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 如果响应状态码不是200，引发HTTPError异常
    response.encoding = response.apparent_encoding  # 设置响应编码

    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 这里可以添加具体的数据提取逻辑，比如提取所有的标题
    titles = soup.find_all('h1')
    for title in titles:
        print(title.text)

    # 模拟随机延迟，避免请求过于频繁
    time.sleep(random.randint(1, 5))
except requests.RequestException as e:
    print(f"请求出错: {e}")
except Exception as ex:
    print(f"发生其他错误: {ex}")


def get_cnki_abstracts(keyword, max_pages=5):
    """
    爬取知网文献摘要
    :param keyword: 搜索关键词
    :param max_pages: 最大爬取页数
    :return: 文献摘要列表
    """
    # 知网搜索URL
    base_url = "https://kns.cnki.net/kns8/kns/brief/result.aspx?dbprefix=scdb"
    
    # 请求头，模拟浏览器访问
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # 搜索参数
    params = {
        'dbprefix': 'scdb',
        'db_opt': 'SCOD',
        'kw': keyword
    }
    
    abstracts = []
    
    try:
        for page in range(1, max_pages + 1):
            print(f"正在爬取第 {page} 页...")
            
            # 设置页码参数
            params['curpage'] = page
            
            # 发送请求
            response = requests.get(base_url, headers=headers, params=params)
            response.encoding = 'utf-8'
            
            # 解析HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 查找文献条目
            items = soup.find_all('tr', class_='odd') + soup.find_all('tr', class_='even')
            
            for item in items:
                # 获取文献标题
                title_tag = item.find('td', class_='name').find('a')
                title = title_tag.get_text(strip=True) if title_tag else "无标题"
                
                # 获取文献链接
                link = "https://kns.cnki.net" + title_tag['href'] if title_tag else "无链接"
                
                # 获取文献摘要
                abstract_tag = item.find('td', class_='info')
                abstract = abstract_tag.get_text(strip=True) if abstract_tag else "无摘要"
                
                # 添加到结果列表
                abstracts.append({
                    'title': title,
                    'link': link,
                    'abstract': abstract
                })
            
            # 随机延迟，避免被封IP
            time.sleep(random.uniform(1, 3))
            
        print(f"爬取完成，共获取 {len(abstracts)} 篇文献摘要")
        return abstracts
        
    except Exception as e:
        print(f"爬取过程中出现错误: {e}")
        return abstracts

def save_abstracts_to_file(abstracts, filename):
    """
    将文献摘要保存到文件
    :param abstracts: 文献摘要列表
    :param filename: 保存文件名
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for i, abstract in enumerate(abstracts, 1):
                f.write(f"第 {i} 篇文献\n")
                f.write(f"标题: {abstract['title']}\n")
                f.write(f"链接: {abstract['link']}\n")
                f.write(f"摘要: {abstract['abstract']}\n")
                f.write("-" * 50 + "\n")
        print(f"文献摘要已保存到文件: {filename}")
    except Exception as e:
        print(f"保存文件时出现错误: {e}")

if __name__ == "__main__":
    # 示例用法
    keyword = "人工智能"
    max_pages = 3
    
    print(f"开始爬取知网关于 '{keyword}' 的文献摘要...")
    abstracts = get_cnki_abstracts(keyword, max_pages)
    
    if abstracts:
        save_abstracts_to_file(abstracts, "cnki_abstracts.txt")
    else:
        print("未获取到任何文献摘要"
## 代码讲解视频台词脚本

### 开场 (0:00-1:30)
"大家好，我是今天的主讲老师。今天我们来学习如何用Python制作一个知网文献摘要的爬虫程序。这个程序适合大一新生学习，代码简洁易懂，方便大家理解和上手。"

### 程序概述 (1:30-3:00)
"首先，我们来了解一下这个程序的整体功能。这个程序可以根据关键词搜索知网文献，并爬取文献的标题、链接和摘要信息，最后将这些信息保存到一个文本文件中。"

### 环境准备 (3:00-5:00)
"在开始编写代码之前，我们需要准备好Python环境，并安装必要的库。我们需要安装requests和BeautifulSoup库，这两个库分别用于发送HTTP请求和解析HTML内容。"

### 代码结构讲解 (5:00-10:00)
"接下来，我们来看一下程序的整体结构。程序主要分为两个函数：get_cnki_abstracts函数用于爬取文献摘要，save_abstracts_to_file函数用于将爬取到的信息保存到文件中。"

### 详细代码讲解 (10:00-30:00)
"现在，我们来逐行讲解代码。首先是导入必要的库，然后是get_cnki_abstracts函数的实现，包括请求头的设置、参数的传递、HTML的解析等。接着是save_abstracts_to_file函数的实现，用于将爬取到的信息保存到文件中。"

### 运行和测试 (30:00-35:00)
"最后，我们来运行和测试这个程序。我们可以修改关键词和最大爬取页数，然后运行程序，查看爬取结果。"

### 注意事项和扩展 (35:00-40:00)
"在使用这个程序时，需要注意一些事项，比如不要频繁发送请求，避免被封IP。同时，我们还可以对程序进行扩展，比如增加更多的搜索参数，或者将爬取结果保存到数据库中。"

### 结束语 (40:00)
"今天的课程就到这里，希望大家通过这个程序的学习，能够掌握Python爬虫的基本原理和实现方法。如果大家有任何问题，可以在评论区留言，我会尽快回复大家。谢谢大家！"