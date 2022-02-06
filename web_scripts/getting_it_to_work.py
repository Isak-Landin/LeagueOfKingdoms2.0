import os
import pathlib
import shutil
import time
import traceback

path = pathlib.Path(__file__).parent.resolve()
port = 9222
command = fr'start chrome.exe --remote-debugging-port={port} --user-data-dir={path}'\
          + r'\instances_of_chrome' + fr'\{port}'
os.system(command)

print(command)