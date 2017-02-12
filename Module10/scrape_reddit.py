from bs4 import BeautifulSoup as BS
from bs4 import SoupStrainer
import urllib2

test_url = urllib2.urlopen("http://www.reddit.com")
readhtml = test_url.read()
test_url.close()

soup = BS(readhtml,"html5lib")
first_20_a_tags = soup.find_all("a", limit=20)

for links in first_20_a_tags:
    print links.get('href')