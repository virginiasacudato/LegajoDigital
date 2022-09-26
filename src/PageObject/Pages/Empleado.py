from selenium.webdriver.common.by import By
import time
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'C:/Users/Maynar/Desktop/LegajoDigital/.env')
load_dotenv(dotenv_path)

# Environment Variables
USER_EMPLOY = os.getenv('USER_EMPLOY')
PASSWORD_EMPLOY = os.getenv('PASSWORD_EMPLOY')


class Empleado:
    # Caso de prueba para un solo empleado

    # -- Locators --
    def __init__(self, driver):
        self.driver = driver
        # LogOut
        self.exit = '/html/body/main/header/div[2]/i'
        self.confirm = '//*[@id="1"]'
        # Login
        self.user = 'Usuario'
        self.password = 'Password'
        self.btn_ingresar = 'btnIngresar'
        # Documents
        self.mi_documents = '/html/body/main/aside/section/nav/ul/li[3]/div/label'
        self.docs = '/html/body/main/aside/section/nav/ul/li[3]/div/div/ul/li[1]/a'
        # Firmar Doc
        self.firmar_btn = '//*[@id="btnFirmarDocumentacion"]'


    # -- Get Elements --

    # Exit
    def get_btn_exit(self):
        return self.driver.find_element(By.XPATH, self.exit)

    def get_confirm(self):
        return self.driver.find_element(By.XPATH, self.confirm)

    # Login
    def get_user(self):
        return self.driver.find_element(By.ID, self.user)

    def get_password(self):
        return self.driver.find_element(By.ID, self.password)

    def get_btn_ingresar(self):
        return self.driver.find_element(By.ID, self.btn_ingresar)

    # Section
    def get_doc_section(self):
        return self.driver.find_element(By.XPATH, self.mi_documents)

    def get_doc(self):
        return self.driver.find_element(By.XPATH, self.docs)

    def get_firmar_btn(self):
        return self.driver.find_element(By.XPATH, self.firmar_btn)


    # -- Actions --

    def logout_adm(self):
        self.get_btn_exit().click()
        self.get_confirm().click()
        time.sleep(5)

    def login_emp(self):
        self.get_user().send_keys(USER_EMPLOY)
        time.sleep(1)
        self.get_password().send_keys(PASSWORD_EMPLOY)
        self.get_btn_ingresar().click()
        time.sleep(3)

    def select_section_doc(self):
        self.get_doc_section().click()
        self.get_doc().click()

    def sign_doc(self):
        self.get.firmar_doc()












