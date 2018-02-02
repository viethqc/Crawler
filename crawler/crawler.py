import os
import requests
from pyquery import PyQuery
import urllib

try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

class Crawler :
    def __init__(self):
        self.__url = ""
        self.__schema = ""
        self.__serverName = ""
        self.__objectName = ""
        self.__pathStorage = ""

    def setUrl(self, url):
        self.__url = url
        parser = urlparse(url)

        self.__serverName = parser.netloc
        self.__objectName = parser.path
        self.__schema = parser.scheme

    def setPathStorage(self, pathStorage):
        if (os.path.exists(pathStorage) == False) :
            os.makedirs(pathStorage)

        self.__pathStorage = pathStorage
        return True

    def startCrawler(self):
        if self.__url == "" :
            return False

        request = requests.get(self.__url)
        pyquery = PyQuery(request.content)
        listChap = pyquery(".ChI a")
        for i in range(listChap.length) :
            chap = listChap.eq(i)
            self.__singleCrawler(self.__schema + "://" + self.__serverName + chap.attr["href"], os.path.join(self.__pathStorage, chap.text()))
        return ""

    def __singleCrawler(self, link, folder):
        fileDone = os.path.join(folder, "done")
        linkImg = ""
        fileName = ""

        if os.path.exists(folder) == False :
            os.makedirs(folder)

        response = requests.get(link)
        if (response.status_code != 200) : 
            return False

        if os.path.exists(fileDone) == True :
            return True

        pyquery = PyQuery(response.content)
        listImg = pyquery("#ctl14_PC img")
        for i in range(listImg.length) :
            img = listImg.eq(i)
            linkImg = img.attr["src"]
            fileName = os.path.join(folder, str(i) + ".jpg")
            urllib.urlretrieve(linkImg, fileName)

        f= open(fileDone,"w+")
        return True
    