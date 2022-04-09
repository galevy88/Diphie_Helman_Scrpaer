from asyncio.windows_events import NULL
import os
import random
from re import X
from selenium import webdriver
import time

os.environ['PATH'] += r"C:\Program Files (x86)"
amount = 1
digitNumber = 256
timeToSleep = 1

def GenertePrimeNumber():

    driver = webdriver.Chrome()
    driver.get('https://bigprimes.org/')
    time.sleep(timeToSleep)

    amount_web = driver.find_element_by_xpath('//*[@id="numPrimes"]')
    amount_web.send_keys(amount)
    digitNumber_web = driver.find_element_by_xpath('//*[@id="digits"]')
    digitNumber_web.send_keys(digitNumber)

    btn = driver.find_element_by_xpath('//*[@id="wrapper3"]/div/div/div[3]/form/button')
    btn.click()
    time.sleep(timeToSleep)
    PrimeNum = driver.find_element_by_css_selector('.mdl-card__supporting-text').text
    PrimeNum = int(PrimeNum)
    return PrimeNum


class Prime:

    prime = NULL

    def __init__(self):
        self.prime = GenertePrimeNumber()    

    def GetPrime(self):
        return self.prime