#!/usr/bin/env python
# coding: utf-8

# In[2]:


import urllib.request
from bs4 import BeautifulSoup
import json
import time


# In[100]:


# 대분류부터 시작 baseurl, params 세팅

import requests
baseurl = 'https://sell.smartstore.naver.com/api/category-search/'
id = '50000004'
url = baseurl + id
params = {'_action': 'getChild', 'isValid': 'true'}
res = requests.get(url, params=params)

res = res.json()


# In[101]:


# depth2 저장 및 depth2 ids 저장 lastLevel 이 true인 id는 하위 카테고리 조회하지않음

total04 = []
depth2 = []

for list in res:
    total04.append(list)
    if list['lastLevel'] != True:
        depth2.append(list['id'])
    
print(depth2)
print(len(total04))


# In[102]:


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


# In[103]:


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

