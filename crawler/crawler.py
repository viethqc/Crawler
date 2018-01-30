try:
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse

class Crawler :
    def __init__(self):
        self.url = ""
        self.serverName = ""
        self.objectName = ""

    def setUrl(self, url):
        self.url = url
        parser = urlparse(url)

        self.serverName = parser.netloc
        self.objectName = parser.path

        print self.serverName, self.objectName

    def setPathStorage(self, pathStorage):
        return ""

    def startCrawler(self):
        return ""
    