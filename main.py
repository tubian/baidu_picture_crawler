#coding:utf-8
import requests
from  selenium import webdriver
import re
import os
import urllib

class spider(object):

	def __init__(self,target):
		self.siteURL='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1512192026667_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word='+target
	def get_picture_page(self,urls):
		print(urls)
		page=requests.get(url=urls)
		return page.text
	def get_all_image(self,page,name):
		img_pattern=re.compile('https://ss0.*?\.jpg',re.S)
		images=re.findall(img_pattern,page)
		if images :
			print ("图片获取成功!\n")
			number = 1
			print ("发现",name,"图片共有",len(images),"张照片")
			if not os.path.exists('Baidu picture/'):
				os.mkdir('Baidu picture')
			if not os.path.exists('Baidu picture/'+name+'/'):
				os.mkdir('Baidu picture/'+name+'/')
			for imageURL in images:    #保存图片
				splitPath = imageURL.split('.')
				fTail = splitPath.pop()
				if len(fTail) > 3:
					fTail = "jpg"
				fileName = name + "/" + str(number) + "." + fTail
				self.saveImg(imageURL,fileName)
				number += 1	
		else:
			print ("图片获取失败!")
			
	def saveImg(self,image_URL,fileNames):
		u = urllib.request.urlopen(image_URL)
		data = u.read()
		f = open('Baidu picture/'+fileNames, 'wb')
		f.write(data)
		print ("正在保存图片:"+fileNames+'')
		f.close()

targets=input('搜索内容:')
sp=spider(targets)
pages=sp.get_picture_page(sp.siteURL)
sp.get_all_image(pages,targets)














