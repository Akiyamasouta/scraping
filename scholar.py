from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

def get_search_results(keyword, number):
    columns = ["order", "title", "year", "citations", "url"]
    table = pd.DataFrame(columns=columns)
    html = requests.get("https://scholar.google.co.jp/scholar?hl=ja&as_sdt=0%2C5&num=" + str(number) + "&q=" + keyword).text
    soup = BeautifulSoup(html, "html.parser")
    tags1 = soup.find_all("h3", {"class":"gs_rt"}) #title, url
    tags2 = soup.find_all("div", {"class": "gs_a"}) #writer, year
    tags3 = soup.find_all(text=re.compile("引用元")) #citation
    order = 1
    for tag1, tag2, tag3 in zip(tags1, tags2, tags3):
        title = tag1.text
        url = tag1.select("a")[0].get("href")
        writer = tag2.text
        writer = re.sub(r'\d', '',writer)
        year = tag2.text
        year = re.sub(r'\D', '', year)
        citations = tag3.replace("引用元", "")
        se = pd.Series([order, title, writer, citations, url], columns)
        table = table.append(se, columns)
        order += 1
    return table

keyword = "Pose estimation"
number = 10
search_results  = get_search_results(keyword, number)
filename = keyword + ".xlsx"
search_results.to_excel(filename, encoding='utf-8')