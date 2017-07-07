#coding:utf-8
import urllib2     
req = urllib2.urlopen('http://joanliu7617.blog.163.com/blog/static/101329912201752914639698/')
buf = req.read() 
  
import re
reg1 = 'src="(http://imgcdn.*?\.jpg)"'
page1 = re.compile(reg1)
listurl = re.findall(page1,buf) 


i = 1  
for url in listurl:  
    f = open(str(i)+'.jpg',"wb") 
    req = urllib2.urlopen(url)   
    buf = req.read()              
    f.write(buf)                  
    i = i + 1 

from bs4 import BeautifulSoup
from distutils.filelist import findall

soup = BeautifulSoup(buf,from_encoding = "gbk")
for tag in soup.find_all('div',class_='para'):
	word = tag.find('div').get_text()
	print word
