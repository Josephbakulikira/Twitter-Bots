import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b

#//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div[ x ]/div/div/div/div[2]/div[1]/div[2]/div/div/span/span

class Interaction:
	def __init__(self, driver):
		self.driver = driver
	def clicker(self):
		partisan = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a/span[2]/span')))
		partisan.click()
		time.sleep(2)
	def follow(self):
		for x in range(20, 40):
			follow_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[2]/section/div/div/div/div[%s]/div/div/div/div[2]/div[1]/div[2]/div/div/span/span' %(x))))
			follow_button.click()
			x += 1
			print('follow ', x ,' persons')
			time.sleep(3)
