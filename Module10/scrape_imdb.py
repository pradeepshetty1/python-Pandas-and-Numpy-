from bs4 import BeautifulSoup as BS
import urllib2

url = "http://www.imdb.com/search/title?genres=action&release_date=2015-01-01,&title_type=feature&user_rating=7.5,10"
    # http://www.imdb.com/search/title?genres=action&release_date=2010-01-01,&title_type=feature&user_rating=6.5,10

connected_url = urllib2.urlopen(url)
readHtml = connected_url.read()

connected_url.close()

soup = BS(readHtml,"html5lib")

print soup.find_all('a')