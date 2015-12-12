import urllib2
from utilityfunctions import *
import os
from bs4 import BeautifulSoup
installproxy()
def processGoogle():
	site="google"
	if not os.path.exists(site):
		os.mkdir(site)
	url="http://research.google.com/pubs/papers.html"
	mainurl="http://research.google.com"
	soup=getsoup(url,site)
	c_tags=getcrudetags(soup,site)
	for tg in c_tags:
		url=mainurl+tg.a['href']
		soup=getsoup(url,site)
		par=soup.find_all('ul',attrs={"class":"pub-list"})[0]
		for ch in par.find_all('li'):
			paperdata={}
			name=ch.find_all('p',attrs={"class":"pub-title"})[0].string
			venue=ch.find_all('p')[-1].string
			authors=[]
			atag=ch.find_all('p')[1]
			#authors.append(atag.string)
			for at in atag.children:
				if (type(at).__name__=='NavigableString'):
					#print removeline(at)
					#print removeline(at).split(",")
					for x in removeline(at).split(","):
						if(len(x)>1):
							authors.append(removeline(x))
				else:
					t=removeline(at.string)
					if len(t)>1:
						authors.append(t)
			print removeline(name)
			print removeline(venue)
			print authors
			print "----"
			

def processYahoo():
	site="yahoo"
	if not os.path.exists(site):
		os.mkdir(site)
	url=""
	return
def processXerox():
	return
processGoogle()