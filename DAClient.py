#!/usr/bin python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from getpass import getpass
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import time
import os

chrome_options = Options()
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://10.100.56.55:8090/httpclient.html");

usr = "USER";
psw = "PASS";

username_box = driver.find_element_by_name('username')
username_box.send_keys(usr)

password_box = driver.find_element_by_name('password')
password_box.send_keys(psw)

login_btn = driver.find_element_by_name('btnSubmit')
login_btn.submit()

time.sleep(3)

driver.close()
