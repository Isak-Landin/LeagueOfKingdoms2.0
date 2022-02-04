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

        for account in accounts:
            account[0].get('https://leagueofkingdoms.com')
            try:
                play_button = WebDriverWait(account[0], 30)\
                    .until(EC.presence_of_element_located((By.XPATH, '//*[@id="top"]/div/div[2]/img[1]')))

                play_button.click()
            except:
                print(traceback.print_exc())
                exit("Couldn't find the play button on the website")
            time.sleep(1000)

starter = start()