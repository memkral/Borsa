# -*- coding: utf-8 -*-
from pyvirtualdisplay import Display
from selenium import webdriver


with Display():
    browser = webdriver.Firefox()

    try:
        browser.get('http://www.google.com')
        print(browser.title)
        browser.save_screenshot("screenshot.png") # bu kısmı ben ekledim, bu kod selenium modülünün bir fonksiyonu. Bu kod o anda ki ekranın resmini kayıt ediyor.

    finally:
        browser.quit()