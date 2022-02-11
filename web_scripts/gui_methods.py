import pyautogui
import pygetwindow
import cv2
import traceback
import time
import pathlib


PATH_web_scripts = str(pathlib.Path().resolve()) + r'\web_scripts'

def focus(window_id):
    window_id.minimize()
    time.sleep(1)
    window_id.restore()
    time.sleep(0.1)

    tries = 0

    while window_id.isActive is False and tries < 5:
        window_id.minimize()
        time.sleep(0.5)
        window_id.restore()

        tries += 1


def login_window(account_settings, accounts_temp_data, key_account):
    logged_in = False
    try:
        if account_settings[key_account]['login_method'] == 'google':
            logged_in = clicking_login_method(login_method=account_settings[key_account]['login_method'],
                                              browser_window=accounts_temp_data[key_account]['window_id'])
        elif account_settings[key_account]['login_method'] == 'apple':
            logged_in = clicking_login_method(login_method=account_settings[key_account]['login_method'],
                                              browser_window=accounts_temp_data[key_account]['window_id'])
        elif account_settings[key_account]['login_method']:
            logged_in = clicking_login_method(login_method=account_settings[key_account]['login_method'],
                                              browser_window=accounts_temp_data[key_account]['window_id'])
        elif account_settings[key_account]['login_method']:
            logged_in = clicking_login_method(login_method=account_settings[key_account]['login_method'],
                                              browser_window=accounts_temp_data[key_account]['window_id'])

    except:
        print(traceback.print_exc())
        print("Couldn't login with login_window for: ", account_settings)

    finally:
        return logged_in


def clicking_login_method(login_method, browser_window):
    logged_in = False
    try:
        window = browser_window  # get window id and region of current selenium window
        focus(window)

        region = (window.topleft[0], window.topleft[1], window.width, window.height)

        login_button = pyautogui.locateOnScreen(PATH_web_scripts + '\\' + f'{login_method}.png',
                                                region=region,
                                                confidence=0.85)

        counter = 0
        while login_button is None and counter < 5:
            print('Looking in', )
            login_button = pyautogui.locateOnScreen(PATH_web_scripts + '\\' + f'{login_method}.png',
                                                    region=region,
                                                    confidence=0.85)

            counter += 1

        pyautogui.moveTo(login_button, duration=1)
        time.sleep(0.2)
        pyautogui.click()

        # Expect something to appear, if it doesn't make sure to retry

        logged_in = True

    except:
        print(traceback.print_exc())
        print('Could not complete login action for', login_method, browser_window)
        pass

    finally:
        # temporary sleep
        time.sleep(15)
        return logged_in


def calculate_region(window):
    region = (window.topleft[0], window.topleft[1], window.width, window.height)
    return region




