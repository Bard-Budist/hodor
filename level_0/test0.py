#!/usr/bin/python3
import requests
url = "http://158.69.76.135/level0.php"
with requests.session() as client:
	data = {
		"id": 1192,
		"holdthedoor": "submit"
		}
	for cont in range(1024):
		client.post(url, data)