import os
import urllib
import urllib2
from bs4 import BeautifulSoup

url = "http://localhost:8080/senimg.html"

html = urllib2.urlopen(url)
soup = BeautifulSoup(html)

# for link in soup.find_all("a"):
#    print "http://legislature.vermont.gov" + str(link.get('href'))

#for td in soup.find_all("td", class_="sorting_1"):
#    for a in td.find_all("a"):
#        print "<a href='http://legislature.vermont.gov" + str(a.get("href")+"'></a>")

imagenum = 0

for td in soup.find_all("td", class_="sorting_1"):
    for a in td.find_all("a"):
        url='http://legislature.vermont.gov'+ str(a.get("href"))
        soup1=BeautifulSoup(urllib2.urlopen(url).read())
        link = soup1.find(class_="profile-photo")
        imglink="http://legislature.vermont.gov" + str(link["src"])

        urllib.urlretrieve(imglink, str(imagenum))
        imagenum=imagenum+1
