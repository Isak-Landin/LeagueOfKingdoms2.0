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

PATH_web_scripts = str(pathlib.Path().resolve())
PATH_json_configs = str(pathlib.Path().resolve()) + r'\account_settings.json'


class Start:
    def __init__(self):
        self.all_selenium_to_devtools_list = []

        with open(PATH_json_configs, 'r+') as file:
            self.data = json.load(file)

        print(self.data)
        self.length_accounts = len(self.data)

    def start_selenium_port(self):
        for i in range(self.length_accounts):
            port = "800" + str(i)
            driver = exe_chrome.start_chrome(port=port)

            dev_tools = pychrome.Browser(url=f"http://localhost:{port}")

            self.all_selenium_to_devtools_list.append([driver, dev_tools, self.data[i]])

            return self.all_selenium_to_devtools_list

    def login_to_kingdom(self):
        instances = self.all_selenium_to_devtools_list

        # Entering www.leagueofkingdoms.com and clicking play, then exiting first tab
        for instance in instances:
            instance[0].get('https://leagueofkingdoms.com')
            try:
                play_button = WebDriverWait(instance[0], 30)\
                    .until(EC.presence_of_element_located((By.XPATH, '//*[@id="top"]/div/div[2]/img[1]')))

                play_button.click()

                # Get both open tabs and change the handle to the new tab
                both_handles = instance[0].window_handles
                current_handle = instance[0].current_window_handle

                # Switch handle
                for new_handle in both_handles:
                    # switch focus to child window
                    if new_handle != current_handle:
                        instance[0].switch_to.window(new_handle)

                print('both handles: ', both_handles)

                tabs = instance[1].list_tab()
                print(tabs)
                instance[1].close_tab(tab_id=tabs[1])
                tabs = instance[1].list_tab()
                print(tabs)

                print('Now you should only be seeing the loading screen,'
                      ' if you are seeing another tab please contact me')

            except:
                print(traceback.print_exc())
                exit("Uh oh, something went wrong")

        for instance in instances:
            try:
                disable_notifications = WebDriverWait(instance[0], 200)\
                    .until(EC.presence_of_element_located((By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')))
                disable_notifications.click()
            except:
                print(traceback.print_exc())
                print(f'We could not find the notifications button for the given time-span for {instance[0]}')
                continue

        for instance in instances:
            pass
