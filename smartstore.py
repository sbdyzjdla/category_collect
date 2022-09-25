#!/usr/bin/env python
# coding: utf-8

# In[130]:


import urllib.request
from bs4 import BeautifulSoup
import json
import time


# In[171]:


# 대분류부터 시작 baseurl, params 세팅

import requests

rooturl = 'https://sell.smartstore.naver.com/api/category-search/'
id = '50000002'
rparams = {'isValid': 'true'}
res = requests.get(rooturl+id, params=rparams)
res = res.json()

total04 = []
total04.append(res)

baseurl = 'https://sell.smartstore.naver.com/api/category-search/'
url = baseurl + id
params = {'_action': 'getChild', 'isValid': 'true'}
res = requests.get(url, params=params)
res = res.json()


# In[172]:


# depth2 저장 및 depth2 ids 저장 lastLevel 이 true인 id는 하위 카테고리 조회하지않음


depth2 = []

for list in res:
    total04.append(list)
    if list['lastLevel'] != True:
        depth2.append(list['id'])
    
print(depth2)
print(len(total04))


# In[173]:


# depth3 저장 및 depth3 ids 저장 astLevel 이 true인 id는 하위 카테고리 조회하지않음

depth3 = []
params = {'_action': 'getChild', 'isValid': 'true'}
res = requests.get(url, params=params)

for idx in depth2:
    params = {'_action': 'getChild', 'isValid': 'true'}
    res = requests.get(baseurl + idx, params=params)
    print(res.json())
    print()
    for list in res.json():
        total04.append(list)
        if list['lastLevel'] != True:
            depth3.append(list['id'])


# In[174]:


# depth4 카테고리 저장

for idx in depth3:
    params = {'_action': 'getChild', 'isValid': 'true'}
    res = requests.get(baseurl + idx, params=params)
    print(res.json())
    print()
    for list in res.json():
        total04.append(list)
        print(list)
        print()


# In[175]:


# 'id' -> '_id'
# False -> false
# True -> true

print(total04)

file_path =  '/Users/yoonsungoh/Documents/develope/category/화장품.json'

with open(file_path, 'w') as outfile:
    json.dump(total04, outfile, indent=4 ,ensure_ascii=False)


# In[ ]:




