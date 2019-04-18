# 功能 #
- 搜索当前目录下所有文件为targetEncodeType编码格式
- 转码UTF-8文件

## 配置项 ##
在文件config.json里，默认配置文件在当前目录.   
* 编码类型：targetEncodeType = 'utf-8'    
* 文件类型：fileType = ['.txt', '.json', '.cs', '.go', '.lua', '.proto']    

# fileWatcher.py #
## 功能 ##
遍历当前目录所有文件，满足fileType类型的文件是否满足编码类型targetEncodeType。如果不满足感兴趣的编码类型，就输出日志到结果集文件"result.txt"。  

## 使用 ##
可以直接运行编译好的exe。默认配置和检索路径都是当前目录下。  

## 结果集合 ##
例子：  
path=C:\Users\duoyi\Desktop\fileWatcher\hehe.txt, type=.txt, encode=ISO-8859-1

意为：  
路径的文件C:\Users\duoyi\Desktop\fileWatcher\hehe.txt，文件类型为 .txt，编码类型为 ISO-8859-1

# convert2utf8.py #
## 功能 ##
遍历当前目录所有文件，满足fileType类型的文件且编码不符合UTF-8标准的，就转换为"utf-8"编码格式文件，所有被转换的文件信息会被输出日志到结果集文件"transform.txt"。  

## 使用 ##
可以直接运行编译好的exe。默认配置和检索路径都是当前目录下。  

## 结果集合 ##
例子：  
path=C:\Users\duoyi\Desktop\fileWatcher\hehe.txt, type=.txt, encode=ISO-8859-1

意为：  
处理了路径C:\Users\duoyi\Desktop\fileWatcher\hehe.txt的文件，文件类型为 .txt，编码类型为 ISO-8859-1