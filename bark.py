'''
Description: 
Version: 2.0
Autor: xinmang
Date: 2021-04-30 01:54:26
LastEditors: xinmang
LastEditTime: 2021-05-10 21:22:13
'''
import requests
import json

bark_url = 'https://'
data = 'message: yys test'
req = requests.get(bark_url + data)
print(json.loads(req.text))