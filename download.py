#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib3 import encode_multipart_formdata
import requests
import os
import time
import sys
import json
'''
下载文件
'''
class Download():
		#初始化类文件
	def __init__(self,api_file_url,headers,cookie):
		self.api_file_url = api_file_url
		self.headers = headers
		self.cookie = cookie
		 
		#执行下载
	def download(self):
		start = time.time()
		#下载文件名
		# print(os.path.split(self.api_file_url))
		# print(os.path.basename(self.api_file_url))
		#获取文件名 e6a59548da20bcf3.mp4?sign=05e6532286c697b10dbcac6761dcac83&t=5bee2e2d
		basename = os.path.basename(self.api_file_url)
		#获取?号的位置
		# pos = basename.find('?')
		#获取文件名
		# file_name = basename[0:pos]
		# print('='*30 +'正在下载:'+file_name + '='*30)
		file_name = os.getcwd() + '/' + basename
		# print(file_name)
		temp_size = 0 #已经下载文件大小
		res = requests.get(self.api_file_url, headers=self.headers)
		chunk_size = 1024 #每次下载数据大小
		total_size = int(res.headers.get("Content-Length"))
		 
		if res.status_code ==200:
			print('[文件大小]:%0.2f MB' %(total_size / chunk_size /1024)) #换算单位并打印
			#保存下载文件
			with open(file_name, 'wb') as f:
				for chunk in res.iter_content(chunk_size=chunk_size):
				    if chunk:
				        temp_size += len(chunk)
				        f.write(chunk)
				        f.flush()
				        #############花哨的下载进度部分###############
				        done = int(50 * temp_size / total_size)
				        # 调用标准输出刷新命令行，看到\r 回车符了吧
				        # 相当于把每一行重新刷新一遍
				        sys.stdout.write("\r[%s%s] %d%%" % ('█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
				        sys.stdout.flush()
			print()  # 避免上面\r 回车符，执行完后需要换行了，不然都在一行显示
			end = time.time() #结束时间
			print('全部下载完成!用时%.2f 秒' %(end-start))
			self.upload2lanzous(basename,file_name,cookie)
		else:
			print(res.status_code)
		 
	def upload2lanzous(self,filename, file_path,cookie):
		"""
		:param filename：文件的名称
		:param file_path：文件的绝对路径
		"""
		print("开始上传")
		url = "https://pc.woozooo.com/fileup.php" # 请求的接口地址
		with open(file_path, mode="r", encoding="utf8") as f: # 打开文件
			file = {
				"file": (filename, f.read()),# 引号的file是接口的字段，后面的是文件的名称、文件的内容
				"task": "1",
				"folder_id": -1,
				"id":"WU_FILE_0",
				"name": filename, # 如果接口中有其他字段也可以加上
				} 
		print(filename)
		encode_data = encode_multipart_formdata(file)
		file_data = encode_data[0] 
		# b'--c0c46a5929c2ce4c935c9cff85bf11d4\r\nContent-Disposition: form-data; name="file"; filename="1.txt"\r\nContent-Type: text/plain\r\n\r\n...........--c0c46a5929c2ce4c935c9cff85bf11d4--\r\n
		
		headers_from_data = {
			"Content-Type": "application/x-www-form-urlencoded", 
			"User-Agent":"Opera/9.80 (Windows NT 6.2; Win64; x64) Presto/2.12.388 Version/12.15",
			"Cookie":cookie,
			"Referer":"https://pan.lanzous.com",
			"Accept-Language":"zh-CN,zh;q=0.9",
			} 
		# token是登陆后给的值，如果你的接口中头部不需要上传字段，就不用写，只要前面的就可以
		# 'Content-Type': 'multipart/form-data; boundary=c0c46a5929c2ce4c935c9cff85bf11d4'，这里上传文件用的是form-data,不能用json
		
		response = requests.post(url=url, headers=headers_from_data, data=file_data).json()
		print("回执消息")
		print(response)
		return response
		
	
if __name__ == "__main__":
		param_url = sys.argv[1]
		print(sys.argv)
		response = requests.get(param_url)
		print(response.text)
		datas = json.loads(response.text)
		headers = eval(datas["headers"])
		segmentfault = Download(datas["url"],headers,datas["cookie"])
		segmentfault.download()