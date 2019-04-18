#-*- encoding=utf8 -*-
import sys
import os
import urllib.request
import requests
import matplotlib.pyplot as plt #约定俗成的写法plt
import re # 正则
import string
from datetime import datetime, date, timedelta	# 时间
from bs4 import BeautifulSoup
from lxml import etree
from urllib.parse import quote

# 绘图设置中文字体
plt.rcParams['font.sans-serif']=['SimHei'] 	#用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False 	#用来正常显示负号

# todo:今天的url
srcUrl = "http://xxx.xxxx.com:xxxxx/xx/xx/"

tmpDay = date.today()
tmpY = str(tmpDay.year)
tmpM = str(tmpDay.month).zfill(2)
tmpD = str(tmpDay.day).zfill(2)

matchUrl = "{0}{1}{2}{3}".format(srcUrl,tmpY, tmpM, tmpD)

urlList = []

for i in range(1,25):
	urlList.append(matchUrl+str(i).zfill(2))

# todo:http前缀
urlHeader = "http://xxx.xxxx.com:xxxxx"

# todo:ping文件正则
matchPattern = "/(.*)_netping2_(.*)\.txt$"
matchCom = re.compile(matchPattern)

# todo:ping文件名字正则
fileTitlePattern = "/xx/xx/(.*)/(.*)_netping2_(.*)\.txt$"
fileTitleCom = re.compile(fileTitlePattern)

# 日期文件夹正则
dirPattern = "/(\d+)"
dirCom = re.compile(dirPattern)

# 新生成计数
newerCount = 0

# 循环取url
for i, dateUrl in enumerate(urlList):
	# 本地文件夹路径
	fileDirStr = "".join(dirCom.findall(dateUrl))
	dataPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), fileDirStr)

	# 所有日期的文件夹链接
	srcList = requests.get(dateUrl)
	srcSoup = BeautifulSoup(srcList.text, 'lxml')
	# 遍历所有日期的链接
	for a in srcSoup.find_all('a'):
		dirLink = a['href']
		if matchCom.match(dirLink):
			# 如果没有文件夹就创建
			if os.path.exists(dataPath) == False:
				print("dataPath:{0}, not exists, creating...".format(fileDirStr))
				os.makedirs(dataPath)
			#  如果该文件已存在,就跳过. todo
			title = "".join(fileTitleCom.findall(dirLink)[0]).replace(":", "_")
			fileName =  dataPath+"\\"+title+".png"
			if os.path.exists(fileName):
				print("file exists:", title)
				continue
			fileUrl = quote(urlHeader+dirLink, safe=string.printable)
			with urllib.request.urlopen(fileUrl) as response:
   			 	# 序号、Rtt、ping列表
				countList,rttList,pingList = [],[],[]
				for i, value in enumerate(str(response.read()).split("|")):
					value = value.split(",")
					if len(value) >= 3:
						countList.append(int(value[0].replace("b\'","").replace("\\n","")))
						rttList.append(int(value[1]))
						pingList.append(int(value[2]))
				plt.figure(figsize=(15,10))
				plt.plot(countList,rttList,"b-")
				plt.plot(countList,pingList,"r-")
				plt.xlabel("时序")	#宋体
				plt.ylabel("ping")	#黑体
				plt.title(title)
				# 设置坐标轴范围
				plt.ylim((-1, 1000))
				# 设置坐标轴刻度
				plt.yticks([-1, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 1000])
				plt.savefig(fileName)
				newerCount = newerCount + 1 
				# plt.show()
print("新生成了{0}张ping图哟 ╮(╯▽╰)╭".format(newerCount))
