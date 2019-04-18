import chardet
import os
import json

# 配置文件,默认当前目录下
fwConfig = json.load(open(os.getcwd() + "\config.json", encoding="utf-8"))

# 是否忽略文件类型
ignoreFileType = True

# 生成结果文件
f = open("result.txt", "w")
f.write("--------------------- Test Begin -----------------------\n")


# 获取文件编码类型
def get_encoding(file):
	# 二进制方式读取, 获取字节数据, 检测类型
	with open(file, "rb") as f:
		data = f.read()
		return chardet.detect(data)['encoding']


# 递归判断文件类型
def print_dir(dir):
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
			if encode != fwConfig["targetEncodeType"]:
				try:
					with open(path, "rb") as tmpFile:
						tmpFile.read().decode("utf-8")
				except:
					str = "path={0}, type={1}, encode={2}".format(path, fType, encode)
					print(str)
					f.write(str + '\n')
		else:
			print_dir(path)


print_dir(os.getcwd())
f.write("--------------------- Test End -----------------------\n")
f.close()

input("Press <Enter> to shutdown.")
