#!/usr/bin/python3
from Screenshot import Screenshot_Clipping
from selenium import webdriver

image = Screenshot_Clipping.Screenshot()
driver = webdriver.Firefox()
url = "http://158.69.76.135/level3.php"
driver.get(url)
img_url=image.full_Screenshot(driver, save_path=r'.', image_name='Myimage.png')
print(img_url)
driver.close()

driver.quit()