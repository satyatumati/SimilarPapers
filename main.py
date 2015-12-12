import urllib2
import os
from bs4 import BeautifulSoup

def processGoogle():
	site="google"
	os.mkdir(site)
	url="http://research.google.com/pubs/papers.html"
	mainurl="http://research.google.com"
	soup=getsoup(url,site)
	c_tags=getcrudetags(soup,site)
	for tg in c_tags:
		url=mainurl+tg.a['href']
		soup=getsoup(url,site)
		par=soup.find_all('ul',attr={"class":"pub-list"})[0]
		for ch in par.find_all('li'):
			paperdata={}
			name=ch.find_all('p',attrs={"class":"pub-title"})[0].string
			venue=ch.find_all('p')[-1].string
			authors=[]
			atag=ch.find_all('p')[1]
			authors.append(atag.string)
			for at in atag.find_all('a'):
				authors.append(removeline(at.string))
			print removeline(name)
			print removeline(venue)
			print authors
			print "----"
			

def processYahoo():

def processXerox():
processGoogle()