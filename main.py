import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import login
import interaction

driver = 0
username = ''
password = ''

def main():
	global driver

	print("processing")
	driver = webdriver.Chrome("D:/chromedriver.exe")
	log = login.Login(driver, username, password)
	log.signin()
	driver.get('https://mobile.twitter.com/unity3d')
	time.sleep(3)
	interact = interaction.Interaction(driver)
	interact.clicker()
	interact.follow()

	time.sleep(5)
	print ('kana kata')


if __name__ == "__main__":
	main()
