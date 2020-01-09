import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b

class Login:
	def __init__(self,driver,username,password):
		self.driver = driver
		self.username = username
		self.password = password

	def signin(self):
		self.driver.get('https://mobile.twitter.com/login')

		uid = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > div > div > div.css-1dbjc4n.r-1pi2tsx.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(6) > label > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input')))
		uid.click()
		uid.send_keys(self.username)

		motdepasse = self.driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-1pi2tsx.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(7) > label > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input')
		motdepasse.click()
		motdepasse.send_keys(self.password)

		btn =  self.driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-1pi2tsx.r-13qz1uu.r-417010 > main > div > div > form > div > div:nth-child(8) > div > div')
		btn.click()
		time.sleep(5)