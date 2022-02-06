import os
import pathlib
import shutil
import time
import traceback
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

path = str(pathlib.Path(__file__).parent.resolve())
path_to_chrome_instances = path + r'\instances_of_chrome'


def remove_all_existing_instances():
    all_instances = os.listdir(path_to_chrome_instances)

    if len(all_instances) != 0:
        for file in all_instances:
            try:
                os.remove(path=path_to_chrome_instances + '\\' + str(file))
            except:
                try:
                    shutil.rmtree(path_to_chrome_instances + '\\' + str(file))

                except:
                    print(traceback.print_exc())
                    time.sleep(10)


def start_chrome(port):
    driver = None
    try:
        command = fr'start chrome.exe --remote-debugging-port={port} --user-data-dir={path}' \
                  + r'\instances_of_chrome' + fr'\{port}'
        print('Creating directory')
        new_directory = path_to_chrome_instances + fr'\{port}'
        print(new_directory)
        os.mkdir(new_directory)
        print(command)
        os.system(command)

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")

        driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    except:
        print(traceback.print_exc())

    finally:
        if driver is not None:
            return driver



