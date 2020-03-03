import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

file1 = open("links.txt","r")

links_arr = []
links_arr = file1.readlines()

for link in links_arr:
	# my_url = 'https://tasty.co/recipe/one-pot-mexican-quinoa'
	temp_url = ''
	temp_url = link[:-1]
	my_url = temp_url

	#opening up connection, then grabbing the page
	uClient = uReq(my_url) 
	page_html = uClient.read()
	uClient.close()

	# html parsing
	page_soup = soup(page_html, "html.parser")

	containers = page_soup.findAll("div", {"class":"recipe-header--content header xs-mx2 xs-mb3 md-mb4 md-mt2 lg-mb4"})
	title_container = containers[0]
	recipe_title = title_container.h1.text # get the actual name of the recipe

	ingredient_containers = page_soup.findAll("div", {"class" : "col md-col-4 xs-mx2 xs-mt2 xs-pb3 md-mt0 xs-flex-order-2 md-flex-order-1"}) # get the serving size
	ingredient_container = ingredient_containers[0]

	serving_size = ingredient_container.p.text[4]


	ingredients_containers = page_soup.findAll("li", {"class" : "ingredient xs-mb1 xs-mt0"}) # get the list of ingredients


	ingredient_arr = []

	for ingredient_container in ingredients_containers:
		ingredient_arr.append(ingredient_container.text)


	file2 = open(recipe_title + ".txt", "a")
	for ingredient in ingredient_arr:
		file2.write(ingredient )
		file2.write('\n')





#print(ingredient_arr)

