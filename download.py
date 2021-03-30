#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
import requests
import os
import time
import sys
import upload2lanzous from upload
 
'''
下载文件
'''
class download():
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
                    upload2lanzous(basename,file_name,cookie)
                else:
                    print(res.status_code)
 
 
if __name__ == "__main__":
    api_file_url = sys.argv[0]
    headers = sys.argv[1]
    cookie = sys.argv[2]
    segmentfault = Download(api_file_url,headers,cookie)
    segmentfault.download()