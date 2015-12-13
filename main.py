import urllib2
from utilityfunctions import *
import os
from bs4 import BeautifulSoup
installproxy()
def processGoogle():
	site="google"
	googleData={}
	c=0
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
		googleData[area]=[]
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
			abstag=ch.find_all('a',attrs={"class":"abstract-icon tooltip"})
			abstract="Not found"
			if (abstag):
				abstag=abstag[0]
				absurl=mainurl+abstag['href']
				soup_=getsoup(absurl,site)
				tg=soup_.find_all('div',attrs={"class":"maia-col-8"})

			else:
				nnn=1

			print removeline(name)
			print removeline(venue)
			print authors
			print area
			paperdata['name']=removeline(name)
			paperdata['area']=removeline(area)
			paperdata['authors']=authors
			paperdata['venue']=removeline(venue)
			googleData[area].append(paperdata)
			c+=1
			printli(c)
			print "----"
			

def processYahoo():
	c=0
	site="yahoo"
	if not os.path.exists(site):
		os.mkdir(site)
	aurl="https://labs.yahoo.com/publications?field_publications_research_area_tid=All&field_publications_date_value[value][year]=&page="
	mainurl="https://labs.yahoo.com"
	for i in range(1):
		printli("page "+str(i))
		url=aurl+str(i)
		soup=getsoup(url,site)
		c_tags=getcrudetags(soup,site)
		for tg in c_tags:
			#print tg.prettify
			container=tg.find_all('div',attrs={"class":"f-c07_main"})
			if not container:
				continue
			#print container
			link=container[0].h3.a
			if(link):
				print " LINK "
				url=mainurl+link['href']
				soup=getsoup(url,site)
				name=soup.find_all('h1',attrs={"class":"f-c09_headline"})[0].string
				abstag=soup.find_all('div',attrs={"class":"f-c09_main"})[0]
				abstract_=abstag.descendants
				#print abstag.prettify()
				abstract="Not FOUND"
				for abspt in abstract_:
					#print abspt.prettify()
					if type(abspt).__name__=='NavigableString':
						if(len(abspt)>20):
							abstract=removeline(abspt)
							break
					else:
						 nnnn=0
						# except Exception:
						# 	#PrintException()
						# 	pass
				venue=soup.find_all('li',attrs={"class":"f-c05_list-item"})[0].h6.string
				venue=removeline(venue)
				artag=soup.find_all('p',attrs={"class":"small breadcrumbs"})[0]
				ar_a=artag.find_all('a')
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
				#print container[0].prettify
				name=container[0].h3.string
				authtgs=tg.find_all('ul',attrs={"class":"f-c05_list"})[0]
				for atg in authtgs.find_all('li'):
					if(atg.a):
						authors.append(removeline(atg.a.string))
					else:
						#print atg.prettify()
						authors.append(removeline(atg.string))
				vtag=tg.find_all('div',attrs={"class":"f-c07_metadata"})[0]
				venue=vtag.h7.string
				abstract="Not found                              "
				#find in the page itself
			print "*********************"
			print name
			print venue
			print authors
			print area
			print abstract
			print "^^^^^^^^^^^^^^^^^^^^"
			c+=1
			printli(c)

	return
def processXerox():
	return
processYahoo()





