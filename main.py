import urllib.request
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/List_of_programming_languages'
soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
langs = soup.select('div.div-col.columns ul li')


for lang in langs:
    langName = BeautifulSoup(
        lang.prettify(), 'html.parser').select('a')
    # Some items do not have "<a href...>" selector
    if len(langName) > 0:
        print(langName[0].string.strip())
    else:
        print(lang.string)
