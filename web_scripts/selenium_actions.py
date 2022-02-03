import PyChromeDevTools
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pychrome
import json
import pathlib

PATH_web_scripts = str(pathlib.Path().resolve())
PATH_json_configs = PATH_web_scripts.replace('web_scripts', 'configs.json')

class start:
    def __init__(self):
        with open(PATH_json_configs, 'r+') as file:
            self.data = json.load(file)

        print(self.data)
        self.length_accounts = len(self.data)

    def start_seleniums_port(self):
        for i in range(self.length_accounts):
            options = webdriver.ChromeOptions()
            options.add_argument(f"--remote-debugging-port=800{str(i)}")


starter = start()