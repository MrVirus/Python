import chardet
import os
import json
import codecs

# 配置文件,默认当前目录下
fwConfig = json.load(open(os.getcwd() + "\config.json", encoding="utf-8"))

# 是否忽略文件类型
ignoreFileType = True

# 生成结果文件
retFile = open("transform.txt", "w")
retFile.write("--------------------- transform Test Begin -----------------------\n")


# 获取文件编码类型
def get_encoding(file):
	# 二进制方式读取, 获取字节数据, 检测类型
	with open(file, "rb") as f:
		data = f.read()
		return chardet.detect(data)['encoding']


# 转换单个文件编码为utf-8
def convent_to_utf8(file):
	# 打开后得到文件内容
	encodeType = get_encoding(file)
	print("file{0}, encode={1}".format(file, encodeType))
	f = open(file, "r+", encoding=encodeType)
	content = f.read()
	f.close()
	# 重写文件
	newF = codecs.open(file, "w", encoding='utf-8')
	newF.write(content)
	newF.close()


# 递归转换文件编码
def convent_dir(dir):
	# 遍历文件夹下所有文件
	list = os.listdir(dir)
	for i in range(0, len(list)):
		path = os.path.join(dir, list[i])
		if os.path.isfile(path):
			print("deal=%s" % path)
			fType = os.path.splitext(path)[1]
			if fType not in fwConfig["fileType"]:
				continue
			encode = get_encoding(path)
			if encode != 'utf-8':
				try:
					with open(path, "rb") as tmpFile:
						tmpFile.read().decode("utf-8")
				except:
					str = "path={0}, type={1}, encode={2}".format(path, fType, encode)
					print(str)
					convent_to_utf8(path)
		else:
			convent_dir(path)


convent_dir(os.getcwd())
retFile.write("--------------------- Test End -----------------------\n")
retFile.close()

input("Press <Enter> to shutdown.")
