from bs4 import BeautifulSoup

edureka_html =  """
                <html><head><title>Courses at Edureka</title></head>
                <p class="title"><b>Edureka offerings</b></p>
                <p class="batch">Subjects taught at Edureka are
                <a class="subject" href="http://www.edureka.co/search/R" id="course1">R</a>,
                <a class="subject" href="http://www.edureka.co/search/Python" id="course2">Python</a> and
                <a class="subject" href="http://www.edureka.co/search/Hadoop" id="course3">Hadoop</a>;
                and batches run every month.</p>
                <p class="title">...</p>
                </html>
                """

#soup = BeautifulSoup('<b><!-- Html Comment--></b>')
#soup = BeautifulSoup(open('sample.html'))
soup = BeautifulSoup(edureka_html,"html5lib")

# extracts first <b> tag in html, prints tag value and type
def read_html():
    tag = soup.a
    print tag
    print type(tag)
    print tag.string
    print tag.attrs

# extracts and prints all elements in html
def extract_elements():
    for element in soup.extract():
        print element

def find_tags(tag_name="html"):
    return soup.find_all(tag_name)

def getParent(tag_name="html"):
    tags = []
    if tag_name != "html":
        tags = find_tags(tag_name)

    if len(tags) > 0:
        return tags[0].parent


print find_tags('p')[-1]
read_html()
extract_elements()
#print getParent('title')
# print (soup.prettify()) # indents html
