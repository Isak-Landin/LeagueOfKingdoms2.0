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
import executing_chrome as exe_chrome
import pygetwindow

PATH_web_scripts = str(pathlib.Path().resolve())
PATH_json_configs = str(pathlib.Path().resolve()) + r'\account_settings.json'


class Start:
    def __init__(self):
        self.session_data = {}
        self.all_selenium_to_devtools_list = []

        with open(PATH_json_configs, 'r+') as file:
            self.data = json.load(file)

        print(self.data)
        self.length_accounts = len(self.data)

        self.all_keys = []

        for key in self.data:
            self.all_keys.append(key)

    def start_selenium_port(self):
        for i in range(self.length_accounts):
            port = "800" + str(i)
            driver = exe_chrome.start_chrome(port=port)

            dev_tools = pychrome.Browser(url=f"http://localhost:{port}")

            self.session_data[self.all_keys[i]] = {}
            self.session_data[self.all_keys[i]]['driver'] = driver
            self.session_data[self.all_keys[i]]['dev_tools'] = dev_tools

            return self.session_data

    def get_to_kingdom(self, accounts):
        instances = accounts

        # Entering www.leagueofkingdoms.com and clicking play, then exiting first tab
        for instance in instances:
            driver = instances[instance]['driver']
            print('This is your driver: ', driver)
            driver.get('https://leagueofkingdoms.com')
            try:
                play_button = WebDriverWait(driver, 30)\
                    .until(EC.presence_of_element_located((By.XPATH, '//*[@id="top"]/div/div[2]/img[1]')))

                play_button.click()

                # Get both open tabs and change the handle to the new tab
                both_handles = driver.window_handles
                current_handle = driver.current_window_handle

                # Switch handle
                for new_handle in both_handles:
                    # switch focus to child window
                    if new_handle != current_handle:
                        driver.switch_to.window(new_handle)

                print('both handles: ', both_handles)

                tabs = instances[instance]['dev_tools'].list_tab()
                print(tabs)
                instances[instance]['dev_tools'].close_tab(tab_id=tabs[1])
                tabs = instances[instance]['dev_tools'].list_tab()
                print(tabs)

                tab = instances[instance]['dev_tools'].list_tab()[0]

                self.session_data[instance]['tab'] = tab

                print('Now you should only be seeing the loading screen,'
                      ' if you are seeing another tab please contact me')

            except:
                print(traceback.print_exc())
                exit("Uh oh, something went wrong")

        for instance in instances:
            driver = instances[instance]['driver']
            try:
                disable_notifications = WebDriverWait(driver, 200)\
                    .until(EC.presence_of_element_located((By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')))
                disable_notifications.click()
            except:
                print(traceback.print_exc())
                print(f'We could not find the notifications button for the given time-span for {instance[0]}')
                continue

        for instance in instances:
            pass
