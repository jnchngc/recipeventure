#grab all the links and write them to a single .txt file


import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.xml-sitemaps.com/download/tasty.co-eee4e733d/sitemap.xml?view=1'

#opening up connection, then grabbing the page
uClient = uReq(my_url) 
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("url")

string1 = 'recipe'
string2 = 'recipes'

ingredient_arr = []

for container in containers:
	if string2 not in container.loc.text:
		if string1 in container.loc.text:
			ingredient_arr.append(container.loc.text)

file1 = open("links.txt","a")

for string in ingredient_arr:
	file1.write(string)
	file1.write('\n')