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

TARGET_URL = 'https://www.google.co.in/'
TARGET_URL = 'https://libgen.is/'

#TARGET_PARSED = urlparse(TARGET_URL)

#print(response.text)
#print('Time to create session')
session = HTMLSession()
#print('Session Created')
response=session.get(TARGET_URL,headers=headers)

response.html.render() # to render any input tags which are generated dynamically

FillIt = FormFiller(urlUniverse=response.text)
FilledData = FillIt.scrapeWebPage()
# this will return a list
# list  will have items = number of forms on the page
# for each form, there will be a list 
# 1.first value of the list is the 'action' of the form
# 2.Middle value will ususally be empty. It will have any hidden inputs which would not have been filled
# 3.last value is the dictionary which will indeed be sent as the POST REQUEST data


FillIt.addSearchQuery([])
# allows addition of seach query

DOMAIN_URL=TARGET_URL # this will be stored by crawler

for everyFormData in FilledData:

    print(everyFormData)
    #print(TARGET_URL)
    if(everyFormData[0] == 'No Action'):
        FillAtURL = DOMAIN_URL #current_url
    else:
        if(everyFormData[0][0] =='/'):
            #print(everyFormData)
            FillAtURL=TARGET_URL+everyFormData[0][1:]
        else:
            FillAtURL=TARGET_URL+everyFormData[0][0:]

    if(everyFormData[1] =='post'):
        print('To POST at : '+FillAtURL)
        new_respone = session.post(FillAtURL,data=everyFormData[-1],headers=headers)
    elif(everyFormData[1] == 'get'):
        GetFromURL = FillAtURL
        print('To GET at : '+GetFromURL)
        new_respone = session.get(GetFromURL,headers=headers,params=everyFormData[-1])
    
    #print(new_respone.text)
    new_res = open('test1.html',mode='w',encoding='UTF-8')
    new_res.write(new_respone.text)
    new_res.close()
    print(new_respone.status_code,' : ',new_respone.reason)





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






