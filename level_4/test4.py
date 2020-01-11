#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

def getProxies(url):
    listProxies = []
    lenCheck = 0
    index = requests.get(url)
    soup = BeautifulSoup(index.content, 'html.parser')
    for i in range(200, 300, 1):
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
print(len(proxies))

#client = requests.session()
#for i in range(1):
#    proxi = {'http': proxies[i], 'https': proxies[i + 1]}
#    key = client.get(url,proxies = proxi)
#    key_dic = key.cookies.get_dict()
#    data_post = {
#		'id': 1,
#		'holdthedoor': "Submit",
#		'key': key_dic['HoldTheDoor']
#	}
#client.post(url, data_post)


