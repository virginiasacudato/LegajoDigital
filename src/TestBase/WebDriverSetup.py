import unittest
from selenium import webdriver
import urllib3
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'C:/Users/Maynar/Desktop/LegajoDigital/.env')
load_dotenv(dotenv_path)

# Environment Variables
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
BASE_URL = os.getenv('URL')


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-loggind"])
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get()
