#!/usr/bin/python3
import requests
import sys
import urllib3

if (len(sys.argv) != 2):
	print("Usage: ./level0.py <ID>")
	sys.exit(1)

url = "http://158.69.76.135/level0.php"
with requests.session() as client:
	data = {
		"id": int(sys.argv[1]),
		"holdthedoor": "submit"
		}
	for cont in range(1024):
		try:
			client.post(url, data)
		except OSError:
			print('\x1b[6;30;41m' + "Network us unreachable" + '\x1b[0m')
			sys.exit(1)
		except urllib3.exceptions.NewConnectionError:
			print('\x1b[6;30;41m' + "New Connection Error" + '\x1b[0m')
			sys.exit(1)
	print('\x1b[6;30;42m' + "Nice, 1024 request" + '\x1b[0m')