#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import os
#ch = __import__('parse_captcha').parse_captcha

url = "http://158.69.76.135/level2.php"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0', 'Referer': 'http://158.69.76.135/level2.php'}

with requests.session() as client:
    for i in range(1):
        key = client.get(url)
        key_dic = key.cookies.get_dict()
		#os.system("wget " + "http://158.69.76.135/captcha.php")
        cookies = key.cookies['HoldTheDoor']
        data_post = {
			"id": 1,
			"holdthedoor": "Submit",
			"key": key_dic['HoldTheDoor']
		}
        client.post(url, data=data_post, cookies={'HoldTheDoor': cookies}, headers=headers)
