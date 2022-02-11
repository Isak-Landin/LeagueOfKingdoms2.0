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
import gui_methods
import network
import pyautogui

PATH_web_scripts = str(pathlib.Path().resolve())
PATH_json_configs = str(pathlib.Path().resolve()) + r'\account_settings.json'
Path_images = PATH_web_scripts + r'\images'


class Start:
    def __init__(self):
        self.all_chrome_windows = []
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

            windows = pygetwindow.getWindowsWithTitle('Chrome')
            window_id = ''

            for window in windows:
                if window not in self.all_chrome_windows:
                    self.all_chrome_windows.append(window)

                    window_id = window

                    # Testing Area

                    print(window.isActive)

            dev_tools = pychrome.Browser(url=f"http://localhost:{port}")

            self.session_data[self.all_keys[i]] = {}
            self.session_data[self.all_keys[i]]['driver'] = driver
            self.session_data[self.all_keys[i]]['dev_tools'] = dev_tools
            self.session_data[self.all_keys[i]]['window_id'] = window_id
            self.session_data[self.all_keys[i]]['ready'] = False
            self.session_data[self.all_keys[i]]['logged_in'] = False

            return self.session_data

    def get_to_kingdom(self, accounts):
        instances = accounts

        # Entering www.leagueofkingdoms.com and clicking play, then exiting first tab
        for instance in instances:
            driver = instances[instance]['driver']
            print('This is your driver: ', driver)
            driver.get('https://leagueofkingdoms.com')
            try:
                play_button = WebDriverWait(driver, 30) \
                    .until(EC.presence_of_element_located((By.XPATH, '//*[@id="top"]/div/div[2]/img[1]')))

                play_button.click()

                # Get both open tabs and change the handle to the new tab
                both_handles = driver.window_handles
                current_handle = driver.current_window_handle

                # Switch handle
                time.sleep(1)
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

                network_tab = network.enable_network(instances[instance]['dev_tools'])

                self.session_data[instance]['tab'] = network_tab

                print('Now you should only be seeing the loading screen,'
                      ' if you are seeing another tab please contact me')

            except:
                print(traceback.print_exc())
                exit("Uh oh, something went wrong")

        for instance in instances:
            driver = instances[instance]['driver']
            try:
                time.sleep(20)
                disable_notifications = WebDriverWait(driver, 200) \
                    .until(EC.presence_of_element_located((By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')))
                disable_notifications.click()
            except:
                print(traceback.print_exc())
                print(f'We could not find the notifications button for the given time-span for {instance[0]}')

                disabled = False
                try:
                    disable_notifications = WebDriverWait(driver, 200) \
                        .until(
                        EC.presence_of_element_located((By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')))

                    while disable_notifications is False:
                        print('Disabling notification pop-up')
                        disable_notifications = WebDriverWait(driver, 200) \
                            .until(
                            EC.presence_of_element_located((By.XPATH, '//*[@id="onesignal-slidedown-cancel-button"]')))

                        disabled = True
                    disable_notifications.click()


                except:
                    print(traceback.print_exc())
                    print(f'We could not find the notifications button for the given time-span for {instance[0]}')
            continue

    def login_kingdom(self, account):
        logged_in = False
        try:

            login_method = self.data[account]['login_method']
            print(account)
            print(self.data[account])
            if self.session_data[account]['logged_in'] is False:

                if login_method == 'google':
                    logged_in = gui_methods.login_window(account_settings=self.data,
                                                         accounts_temp_data=self.session_data,
                                                         key_account=account)
                elif login_method == 'apple':
                    logged_in = gui_methods.login_window(account_settings=self.data,
                                                         accounts_temp_data=self.session_data,
                                                         key_account=account)
                elif login_method == 'email':
                    logged_in = gui_methods.login_window(account_settings=self.data,
                                                         accounts_temp_data=self.session_data,
                                                         key_account=account)
                elif login_method == ' ':
                    logged_in = gui_methods.login_window(account_settings=self.data,
                                                         accounts_temp_data=self.session_data,
                                                         key_account=account)
                else:
                    print('############')
                    print('Are you sure you entered the correct login method? The available ones are google, apple, email')
        except:
            print(traceback.print_exc())

        finally:
            self.data[account]['logged_in'] = logged_in
