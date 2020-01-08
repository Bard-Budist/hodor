#!/usr/bin/python
import requests

url = "http://158.69.76.135/level2.php"

with requests.session() as client:
	user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"
	for i in range(1):
		key = client.get(url)
 		key_dic = key.cookies.get_dict()
		data_post = {
			"id": 20019,
			"holdthedoor": "Submit",
			"key": key_dic['HoldTheDoor']
		}
		headers = {'User-Agent': user_agent}
		client.post(url, data_post, headers)