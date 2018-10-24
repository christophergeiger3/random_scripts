#!/usr/bin/python2
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
from time import sleep
from bs4 import BeautifulSoup as BS

"""
Search for another UCONN affiliate's basic information (e.g. name, email) using selenium

Dependent on selenium, bs4, and getpass (getpass might come with python actually)
"""

search_text = raw_input("Enter name, form, email, or NetID to search for: ")

user = 'cag16156'
password = getpass('Please Input your NetID password (user cag16156): ')
phonebook_site = "https://phonebook.uconn.edu/"

browser = webdriver.Firefox()
browser.get(phonebook_site)

print('Executing...')
print('Navigated to', browser.title)
try:
	WebDriverWait(browser, 10).until(EC.title_is('UCONN Phone Book'))
	login = browser.find_element_by_link_text('Login to include student information')
	print('Found login element')
	login.click()
	print('Logging in.')
	user_form = browser.find_element_by_id('username')
	pass_form = browser.find_element_by_id('password')
	login_link = browser.find_element_by_id('button')
	user_form.send_keys(user)
	pass_form.send_keys(password)
	login_link.click()
	print('Logged in successfully.')
except:
	print("Couldn't find the login element")
	print('Proceeding as if already logged in')

WebDriverWait(browser, 10).until(EC.title_is('UCONN Phone Book'))
search_form = browser.find_element_by_id('basictext')
submit_search = browser.find_element_by_class_name('submit-but')  # Nice one UITS.

search_form.send_keys(search_text)
submit_search.click()

WebDriverWait(browser, 10).until(EC.title_is('UConn Phonebook - Results'))
soup = BS(browser.page_source)

text = soup.get_text()
print(text)

print('-'*60)
snip_start = 540
snip_end = text.index("Campus Information")
print(text[snip_start:snip_end])
print('-'*60)
