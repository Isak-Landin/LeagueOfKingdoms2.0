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


instances_for_accounts = initiate_selenium_actions.session_data

print('This is all the session data: ', instances_for_accounts)

initiate_selenium_actions.get_to_kingdom(accounts=instances_for_accounts)

start_time = time.time()

keys = []
is_logged_in = [False]

for instance in instances_for_accounts:
    keys.append(instance)

while False in is_logged_in:
    is_logged_in = []
    for key in keys:
        instances_for_accounts = initiate_selenium_actions.session_data
        is_logged_in.append(instances_for_accounts[key]['logged_in'])

    for instance in instances_for_accounts:
        initiate_selenium_actions.login_kingdom(account=instance)
        print('INSTANCE:', instance)
