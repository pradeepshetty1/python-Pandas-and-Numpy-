from bs4 import BeautifulSoup as BS
import requests

url = "http://www.imdb.com/search/title"

params = dict()
params['sort'] = 'num_votes'
params['start']= 1
params['year']='2015'
params['title_type'] = 'action'

resp = requests.get(url, params=params)

print resp.url#, resp.content
print
soup = BS(resp.content)
print soup
#print soup.find_all(title="Inside Out (2015)")#Mission: Impossible - Rogue Nation (2015)")

fl = open('movie_titles','w')
for movie_title in soup.find_all('a','title'):
    print movie_title

fl.close()