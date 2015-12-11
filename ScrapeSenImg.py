import os
import urllib
import urllib2
from bs4 import BeautifulSoup

url = "http://localhost:8080/ScrapeSenateHeadshots/senatedirectory.html"

html = urllib2.urlopen(url)
soup = BeautifulSoup(html)


for td in soup.find_all("td", class_="sorting_1"):
    for a in td.find_all("a"):
        url='http://legislature.vermont.gov'+ str(a.get("href"))
        soup1=BeautifulSoup(urllib2.urlopen(url).read())
        link = soup1.find(class_="profile-photo")
        imglink="http://legislature.vermont.gov" + str(link["src"])
        name = soup1.find('h1').string
        urllib.urlretrieve(imglink, name + ".jpg")
