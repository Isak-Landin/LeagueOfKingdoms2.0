import os
import pathlib
import shutil
import time
import traceback

path_to_chrome_instances = str(pathlib.Path(__file__).parent.resolve()) + '\\' + 'instances_of_chrome'


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
                    time.sleep(10)

def start_chrome(port):
    try:
        new_directory = path_to_chrome_instances + '\\' + str(port)
        os.mkdir(new_directory)
        print(f"start chrome.exe -–remote-debugging-port={port} --user-data-dir={new_directory}")
        os.system(f'cmd /k "start chrome.exe -–remote-debugging-port={port} -–user-data-dir={new_directory}"')

    except:
        print(traceback.print_exc())

remove_all_existing_instances()
start_chrome(8002)