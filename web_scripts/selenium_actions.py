import PyChromeDevTools
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pychrome
import json
import pathlib
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import traceback

PATH_web_scripts = str(pathlib.Path().resolve())
PATH_json_configs = PATH_web_scripts.replace('web_scripts', 'configs.json')

class start:
    def __init__(self):
        self.all_selenium_to_devtools_list = []

        with open(PATH_json_configs, 'r+') as file:
            self.data = json.load(file)

        print(self.data)
        self.length_accounts = len(self.data)

        """ Launching all selenium browser---- Equivalent to the number of accounts found in file """
        self. start_selenium_port()
        print(self.all_selenium_to_devtools_list)

        """ Entering leagueofkingdoms and login in to all accounts """
        self.login_to_kingdom()

    def start_selenium_port(self):
        for i in range(self.length_accounts):
            port = "800" + str(i)
            options = webdriver.ChromeOptions()
            options.add_argument(f"--remote-debugging-port={port}")
            driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

            dev_tools = pychrome.Browser(url=f"http://localhost:{port}")

            self.all_selenium_to_devtools_list.append([driver, dev_tools])

    def login_to_kingdom(self):
        accounts = self.all_selenium_to_devtools_list

        # Entering www.leagueofkingdoms.com and clicking play, then exiting first tab
        for account in accounts:
            account[0].get('https://leagueofkingdoms.com')
            try:
                play_button = WebDriverWait(account[0], 30)\
                    .until(EC.presence_of_element_located((By.XPATH, '//*[@id="top"]/div/div[2]/img[1]')))

                play_button.click()

                # Get both open tabs and change the handle to the new tab
                both_handles = account[0].window_handles
                current_handle = account[0].current_window_handle

                # Switch handle
                for new_handle in both_handles:
                    # switch focus to child window
                    if (new_handle != current_handle):
                        account[0].switch_to.window(new_handle)

                print('both handles: ', both_handles)

                tabs = account[1].list_tab()
                print(tabs)
                account[1].close_tab(tab_id=tabs[1])
                tabs = account[1].list_tab()
                print(tabs)

                print('Now you should only be seeing the loading screen,'
                      ' if you are seeing another tab please contact me')

            except:
                print(traceback.print_exc())
                exit("Uh oh, something went wrong")

        for account in accounts:
            try:
                disable_notifications = WebDriverWait(account[0], 200)\
                    .until(EC.presence_of_element_located((By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')))
                disable_notifications.click()
            except:
                print(traceback.print_exc())
                print(f'We could not find the notifications button for the given time-span for {account[0]}')
                continue

        for account in accounts



starter = start()