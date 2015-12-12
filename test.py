from utilityfunctions import *
import json
from bs4 import BeautifulSoup
import traceback
url="https://labs.yahoo.com/publications/5688/graphical-passwords-wild-%E2%80%93-understanding-how-users-choose-pictures-and-passwords"
printli("Extracting soup from :"+url)
soup=getsoup(url)
name=soup.find('h1',attrs={"class":"f-c09_headline"}).string
print "Name:"
print removeline(name)
venue=soup.find('li',attrs={"class":"f-c05_list-item"}).h6.string
print "Venue"
print removeline( venue)
try:
	area=soup.find('p',attrs={"class":"small breadcrumbs"}).find_all('a')[1].string
except Exception:
	area="Miscellaneous"
print removeline(area)
authors=[]
print "Authors :"
for t in soup.find_all('li',attrs={"class":"f-c05_list-item link-wrap"}):
	for ch in t.h6.children :
		print removeline(ch.string)
printli("Success")