#!/usr/bin/python3
import requests
url = "http://158.69.76.135/level2.php"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0', 'Referer': 'http://158.69.76.135/level2.php'}

with requests.session() as client:
    for i in range(10):
        key = client.get(url)
        key_dic = key.cookies.get_dict()
        cookies = key.cookies['HoldTheDoor']
        data_post = {
			"id": 1992221,
			"holdthedoor": "Submit",
			"key": key_dic['HoldTheDoor']
		}
        client.post(url, data=data_post, cookies={'HoldTheDoor': cookies}, headers=headers)s)