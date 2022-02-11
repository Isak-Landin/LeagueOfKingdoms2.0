import pychrome
from selenium import webdriver
import multiprocessing


def output_on_start(**kwargs):
    print('Started', kwargs)

def output_on_end(**kwargs):
    print('Finished', kwargs)


def enable_network(pychrome_instance):
    tab = pychrome_instance.list_tab()[0]
    tab.start()

    tab.call_method('Network.enable', _timeout=200)
    tab.set_listener('Network.requestWillBeSent', output_on_start)
    tab.set_listener('Network.responseReceived', output_on_end)

    return tab

