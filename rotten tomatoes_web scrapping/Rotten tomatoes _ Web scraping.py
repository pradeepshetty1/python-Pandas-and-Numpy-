from urllib2 import *
from bs4 import BeautifulSoup as bs
import string



from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.rottentomatoes.com/top/bestofrt/")

html = driver.page_source
driver.close()

soup = bs(html, 'html5lib')
#
# print soup.prettify()

table1  = soup.find_all('table', class_="table")

table_rows = soup.find_all('tr')

data = []

for table_rows in table1:
    row = table_rows.find_all('a')

    try:
        for info in (row):
            print info.text
            print "++++++++++++++++++++++++++++++++++++"
            data.append(info.text + "+++++++++++++++++++++++++")
            try:
                with open('D:\movies.txt', 'a') as m:
                    sample = m.writelines(info.text)
                    print sample
            except Exception as e:
                pass
    except:
        pass




































    
    
    

    










