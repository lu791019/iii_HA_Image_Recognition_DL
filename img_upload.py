#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os, sys, time
from pyhdfs import HdfsClient
from configparser import ConfigParser
import pyhdfs
import datetime

client = pyhdfs.HdfsClient(hosts="10.120.14.120,50070",user_name="cloudera")
#print(client.get_home_directory())

#print(client.listdir("/user/cloudera"))

start = input('Please Enter to continue',)

#先以當下時間代替才能存取多張 不然會shut down(這邊可自行修改)
t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

client.copy_from_local("C:/Users/Big data/Desktop/iii_HA/CT/DP_model_faster_RCNN/result_img/"+t+".png","/user/cloudera/recog_img_FRCNN/"+t+".png")

