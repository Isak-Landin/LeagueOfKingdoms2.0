import PyChromeDevTools
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pychrome
import json
from web_scripts import selenium_actions


initiate_selenium_actions = selenium_actions.Start()
account_information = initiate_selenium_actions.start_selenium_port()
dict_of_data = {}

for session in account_information:
    dict_of_data[session[2]] = {
        'selenium-session': session[0],
        'dav-tools': session[1]
    }
with open(r'web_scripts\instances.json', 'r+') as file:
    data = json.load(file)
    data.update(dict_of_data)
    file.seek(0)
    json.dump(data, file)