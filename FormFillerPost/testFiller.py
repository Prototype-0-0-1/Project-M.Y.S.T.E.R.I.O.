from bs4 import BeautifulSoup
from requests_html import HTMLSession

#import requests

import random

from postRequestSender.formfill import FormFiller


import sys
##from PyQt4.QtGui import QApplication
##from PyQt4.QtCore import QUrl
##from PyQt4.QtWebKit import QWebPage


from urllib.parse import urlparse,quote
#import pip._vendor.requests


headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"


#sampleFormFillTest = FormFiller(htmlPath='test.html')

TARGET_URL = 'http://www.dctp.ws/wp-login.php?action=register'

TARGET_URL = 'https://www.quora.com/'

#TARGET_PARSED = urlparse(TARGET_URL)
#print(response.text)
#print('Time to create session')
session = HTMLSession()
#print('Session Created')
response=session.get(TARGET_URL,headers=headers)

#6response.html.render()




#print(response.headers)
#print(response.status_code)
#print(response.request.url)


#print(response.text)


##class Client(QWebPage):
##    def __init__(self,url):
##        self.app = QApplication(sys.argv)
##        QWebPage.__init__(self)
##        self.loadFinished.connect(self.on_page_load)
##        self.mainFrame().load(QUrl(url))
##        self.app.exec_()
##
##    def on_page_load(self):
##        self.app.quit()






