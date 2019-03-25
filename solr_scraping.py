import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

chrome_options = Options()
#prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_argument("--headless")
#chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)


columns = ['title','link','author']
df = pd.DataFrame(columns = columns)

driver.get('http://big5.quanben5.com/category/7_1.html')

for i in range(10):
#max to 156 page but this code is only for showing
    if i != 0:
        driver.find_element_by_link_text("下一頁").click()
    print('Scraping page',i+1)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    for list in soup.select('div.c3 > div > div'):
        title = list.h3.a.text
        link = 'http://big5.quanben5.com' + list.h3.a.get("href") + 'xiaoshuo.html'
        author = list.p.span.text
        #print(title,link,author)
        
        tmp = pd.DataFrame([[title,link,author]],columns = columns)
        df = df.append(tmp,ignore_index=True)

df.to_csv('novel_data.csv',sep=',',encoding='utf_8_sig')
#utf_8_sig: to fix Garbled which has shown in Excel

driver.close()
