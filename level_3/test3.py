#!/usr/bin/python3
import requests
import os
from requests import Request, Session
#from parse_captcha import *

strem = None
verify = False
proxies = None
cert = None
timeout = None
url = "http://158.69.76.135/captcha.php"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0', 'Referer': 'http://158.69.76.135/level2.php'}

with requests.session() as client:
    for i in range(5):
       #client.get(url)
       # key_dic = client.cookies.get_dict()
        key = Request('GET',url, cookies= client.cookies.get_dict())
        prepped = client.prepare_request(key)
        resp = client.send(prepped)
        print(resp.cookies)
        print("-------------------")
        print(client.cookies)
        data_post = {
			"id": 1,
			"holdthedoor": "Submit",
			#"key": key_dic['HoldTheDoor']
                        #"captcha": f.read()
		}
        #client.post(url, data=data_post, cookies={'HoldTheDoor': cookies}, headers=headers)
