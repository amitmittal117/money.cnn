import bs4
import re
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook
book = Workbook()
sheet = book.active
my_url = 'http://money.cnn.com/data/markets/dow/?page=1'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers_outer_div = page_soup.findAll("div",{"id":"wsod_indexConstituents"})

print containers_outer_div

# wsod_indexConstituents
