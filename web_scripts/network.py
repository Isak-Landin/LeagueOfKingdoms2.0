import pychrome
from selenium import webdriver
import multiprocessing


ready_to_go = []


def output_on_start(**kwargs):
    print('Started', kwargs)
    check_for_continuation(kwargs)


def output_on_end(**kwargs):
    print('Finished', kwargs)
    check_for_continuation(kwargs)


def enable_network(pychrome_instance):
    tab = pychrome_instance.list_tab()[0]
    tab.start()

    tab.call_method('Network.enable', _timeout=200)
    tab.set_listener('Network.requestWillBeSent', output_on_start)
    tab.set_listener('Network.responseReceived', output_on_end)

    return tab


def check_for_continuation(response, account):
    if response == '':
        return True
    else:
        return False
