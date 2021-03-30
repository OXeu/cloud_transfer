# "Content-Type": "multipart/form-data; boundary=76a22e30da2bb7790828887966871012"
from urllib3 import encode_multipart_formdata
import requests

class upload():
	def upload2lanzous(filename, file_path,cookie):
		"""
		:param filename：文件的名称
		:param file_path：文件的绝对路径
	 	"""
		url = "https://pc.woozooo.com/fileup.php" # 请求的接口地址
    with open(file_path, mode="r", encoding="utf8") as f: # 打开文件
		file = {
				"file": (filename, f.read()),# 引号的file是接口的字段，后面的是文件的名称、文件的内容
				"task": "1",
    		"folder_id": -1,
    		"id":"WU_FILE_0",
    		"name": filename, # 如果接口中有其他字段也可以加上
					} 
		
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
		return response
		
if __name__=='__main__':
    # 上传文件
    res = sendFile(filename, file_path)          # 调用sendFile方法
	print(res)	

