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
		tailurl=tg.a['href']
		area=tailurl.split("/")[-1]
		area=area.split(".")[0]
		url=mainurl+tailurl
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
	url="https://labs.yahoo.com/publications?field_publications_research_area_tid=All&field_publications_date_value[value][year]=&page="
	mainurl="https://labs.yahoo.com"
	for i in range(100):
		print "page "+str(i)
		url=url+str(i)
		soup=getsoup(url)
		c_tags=getcrudetags(soup,site)
		for tg in c_tags:
			container=tg.find_all('div',attrs={"class":"f-c07_main"})[0]
			link=container.h3.a
			if(link):
				print " LINK "
				url=mainurl+link['href']
				soup=getsoup(url)
				name=soup.find_all('h1',attrs={"class":"f-c09_headline"})[0].string
				abstag=soup.find_all('div',attrs={"class":"f-c09_main"})[0]
				abstract=abstag.div.p.string
				venue=soup.find_all('li',attrs={"class":"f-c05_list-item"})[0].h6.string
				venue=removeline(venue)
				artag=soup.find_all('p',attrs={"class":"small breadcrumbs"})
				ar_a=artag.find_all('a'))
				if len(ar_a)>1:
					area=ar_a[1].string
				else:
					area="Undefined"
				authtags=soup.find_all('li',attrs={"class":"f-c05_list-item link-wrap"})
				authors=[]
				for atg in authtags:
					if atg.h6.a:
						authors.append(removeline(atg.h6.a.string))
					else:
						authors.append(removeline(atg.h6.string))
				#go to link
			else:
				print "IN PAGE"
				area="Undefined"
				name=container.h3.string
				authtgs=soup.find_all('ul',attrs={"class":"f-c05_list"})
				for atg in authtgs.find_all('li'):
					if(atg.a):
						authors.append(removeline(atg.a.string))
					else:
						authors.append(removeline(atd.string))
				vtag=tg.find_all('div',attrs={"class":"f-c07_metadata"})
				venue=vtag.h7.string
				abstract="Not found                              "
				#find in the page itself
			print name
			print venue
			print authors
			print area
			print abstract[20]


	return
def processXerox():
	return
processYahoo()





