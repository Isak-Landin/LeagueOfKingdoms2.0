import pyautogui
import pygetwindow
import cv2
import traceback
import time


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


def clicking_login_method(login_method, browser_window):
    logged_in = False
    try:
        window = browser_window  # get window id and region of current selenium window
        focus(window)

        region = (window.topleft[0], window.topleft[1], window.width, window.height)
        login_button = pyautogui.locateOnScreen(f'{login_method}.png', region=region, confidence=0.85)

        counter = 0
        while login_button is None and counter < 5:
            login_button = pyautogui.locateOnScreen(f'{login_method}.png', region=region, confidence=0.85)

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
        return logged_in

def login_window(login_method):
    if login_method == 'google':
        authentication_window = pygetwindow.getWindowsWithTitle()[0]
    elif login_method == 'apple':
        authentication_window = pygetwindow.getWindowsWithTitle()[0]
    elif login_method == 'email':
        authentication_window = pygetwindow.getWindowsWithTitle()[0]
    elif login_method == '':
        authentication_window = pygetwindow.getWindowsWithTitle()[0]