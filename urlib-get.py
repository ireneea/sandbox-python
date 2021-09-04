import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup


def get_url():
    url = input('Enter url: ')
    if url == '':
        url = 'http://www.dr-chuck.com/page1.htm'
    return url

def print_all_links(data):
    # Retrieve all anchor tags
    tags = data('a')
    for tag in tags:
        print(tag.get('href', None))

html = urllib.request.urlopen(get_url()).read()
soup = BeautifulSoup(html, 'html.parser')
print_all_links(soup)
