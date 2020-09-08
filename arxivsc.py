from datetime import datetime
import re
import requests
from googletrans import Translator
from time import sleep

import arxiv

#webhook POST先URL
API_URL = "https://maker.ifttt.com/trigger/arxivLine/with/key/fdpKKfnpX20wqLHVNK2r4zom5lnmyU3jlBVzZ6zAfk2"
#検索ワード
QUERY = "cat:'astro-ph.IM"
result_list = arxiv.query(query=QUERY, max_results=2, sort_by='submittedDate')

translator = Translator()

dt = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
requests.post(API_URL, data={"value1":dt})

def translate_post():
    title_jpn = translator.translate(title, src='en', dest='ja').text
    abst_jpn = translator.translate(abst, src='en', dest='ja').text
    print("---------" + str(count) + "ページ目----------")
    print("author{}".format(author))
    print(url)
    print("title:{}".format(title_jpn))
    print("date:{}".format(date))
    print("Abstract:{}".format(abst_jpn))

    message = "\n".join(["<br>著者: " + author, "<br>タイトル: " + title_jpn, "<br><br>URL: ", url, "<br><br>発行日: " + date, "<br><br>概要: " + abst_jpn])

    requests.post(API_URL, data={"value1":message})
    sleep(5)

count = 1

for result in result_list:
    author = result.author
    url = result.pdf_url
    title = result.title
    date = result.updated
    abst = result.summary

    abst = abst.replace("\n", "")
    translate_post()

    count += 1

print("Done")