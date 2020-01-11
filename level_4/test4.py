#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import os

def getProxies(url):
    listProxies = []
    lenCheck = 0
    index = requests.get(url)
    soup = BeautifulSoup(index.content, 'html.parser')
    for i in range(250, 300, 1):
        results = soup.find_all('tr')[i]
        for x in results:
            x = str(x).replace("<td>", "")
            firtsLetter = x.replace("</td>", "")
            if (firtsLetter[0] >= '0' and firtsLetter[0] <= '9'):
                listProxies.append(firtsLetter)
    print(listProxies)
    return listProxies


url = "http://158.69.76.135/level4.php"
urlProxies = "https://free-proxy-list.net/index.html"

proxies = getProxies(urlProxies)
with requests.session() as client:
    for i in range(1):
        os.system("unset HTTP_PROXY")
        key = client.get(url)
        key_dic = key.cookies.get_dict()
        cookies = key.cookies['HoldTheDoor']
        data_post = {
			"id": 1,
			"holdthedoor": "Submit",
			"key": key_dic['HoldTheDoor']
		}
        os.environ["HTTP_PROXY"] = "http://" + proxies[4] + ":" + proxies[5]
        #os.system("export HTTP_PROXY=" + '"' +"http://" + proxies[0] + ":" + proxies[1] + '"')
        print(client.post(url, data=data_post))