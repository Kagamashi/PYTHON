# BeautifulSoup
# BeautifulSoup is used for web scraping purposes to extract data from HTML and XML files.
from bs4 import BeautifulSoup  # type: ignore
html_doc = "<html><head><title>The Title</title></head><body><p>Test</p></body></html>"
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.title.string)
