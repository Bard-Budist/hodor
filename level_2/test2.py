#!/usr/bin/python3
import requests

url = "http://158.69.76.135/level1.php"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0'}

with requests.session() as client:

	for i in range(1):
		key = client.get(url)
		key_dic = key.cookies.get_dict()
		data_post = {
			"id": 1,
			"holdthedoor": "Submit",
			"key": key_dic['HoldTheDoor']
		}
		client.post(url, data_post, headers=headers)