import PyChromeDevTools
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pychrome
import json
from web_scripts import selenium_actions
from web_scripts import executing_chrome as exe_chrome
import network

exe_chrome.remove_all_existing_instances()
initiate_selenium_actions = selenium_actions.Start()
account_information = initiate_selenium_actions.start_selenium_port()
dict_of_data = {}

for session in account_information:
    dict_of_data[session[2]] = {
        'selenium-session': session[0],
        'dev-tools': session[1]
    }
instances_for_accounts = initiate_selenium_actions.session_data

print('This is all the session data: ', instances_for_accounts)

initiate_selenium_actions.get_to_kingdom(accounts=instances_for_accounts)

start_time = time.time()
while False in network.ready_to_go and time.time() - start_time < 600:
    time.sleep(5)
