import urllib2
from bs4 import BeautifulSoup
from pyPdf import PdfFileWriter, PdfFileReader
import logging
import linecache
import sys
import os.path
import re
logging.basicConfig(level=logging.INFO)
def getcode(url,site):
	x=url.split("/")[-1]
	x=x.split(".")[0]
	return site+"_"+x
def printli(st):
	logging.info(st)
def installproxy():
	proxy_support = urllib2.ProxyHandler({})
	opener = urllib2.build_opener(proxy_support)
	urllib2.install_opener(opener)
def getsource(url):
	#print url
	r = urllib2.urlopen(url)
	return r.read()
def getcrudetags(soup,site):
	if(site=="google"):
		return soup.find_all("li",attrs={"class":"research-area"})
	elif(site=="yahoo"):
		return soup.find_all(attrs={"class":"f-c07_inner"})
def removeline(s):
	s=s.strip()
	s=" ".join(s.split())
	return s
def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i)<128)
def getsoup(url,site):
	print url
	code=getcode(url,site)
	fil=site+"/"+code+".html"
	if(os.path.isfile(fil)):
		print "found"
		page=open(fil,'r').read()
	else:
		print "notfound"
		page=getsource(url)
		f=open(fil,'w+')
		f.write(page)

	#print page
	page=remove_non_ascii(page)
	page=re.sub('</?em>','',page)
	page=re.sub('</?br /?>','',page)
	page=re.sub('</?br/?>','',page)
	#print "**************"
	#print page
	return BeautifulSoup(page,'html.parser')
def getlist(s):
	l=s.split(',')
	l=[a.strip() for a in l]
	l2=[]
	#print l
	for a in l:
		l2=l2+a.split('and')
		#print l2
	l=[a.strip() for a in l2]
	return l

def PrintException():
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    print 'EXCEPTION IN ({}, LINE {} "{}"): {}'.format(filename, lineno, line.strip(), exc_obj)

def getPDFContent(url,site):
	webFile = urllib.urlopen(url,site)
	path=site+"/"+getcode(url)+".pdf"
	if not os.path.exists(path):
		pdfFile = open(path,'w')
		pdfFile.write(webFile.read())
		webFile.close()
		pdfFile.close()
	pdfFile=open(path,'r')
	inp = PdfFileReader(file(pdfFile, "rb"))
	return inp
