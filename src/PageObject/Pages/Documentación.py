from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait



class Documentacion:

    # -- Locators --
    def __init__(self, driver):
        self.driver = driver
        # Button Menu
        self.documentacion = '/html/body/main/aside/section/nav/ul/li[7]/div/div/ul/li[2]/a'
        self.inpt_file = '//*[@id="divRecuperarArchivos"]/div/input'
        self.check_emp = 'checkbox'
        self.btn_save = 'firmar-y-guardar'
        self.msg_exitoso = '//*[@id="modal-procesar-respuesta"]/div[2]/div/div[1]/h4'


    # -- Get Elements --
    def get_documentacion(self):
        return self.driver.find_element(By.XPATH, self.documentacion)

    def get_inpt_files(self):
        return self.driver.find_element(By.XPATH, self.inpt_file)

    def get_check_emp(self):
        return self.driver.find_elements(By.CLASS_NAME, self.check_emp)

    def get_save_btn(self):
        return self.driver.find_element(By.ID, self.btn_save)

    def get_msg_exitoso(self):
        return self.driver.find_element(By.XPATH, self.msg_exitoso)

    # -- Actions --

    def upload_file(self):
        def check_exito():
            try:
                msg = self.get_msg_exitoso().text
                if msg == 'Operación Exitosa':
                    print('Coincide --> Operacion Exitosa')
            except NoSuchElementException:
                return False
            return True

        self.get_documentacion().click()

        self.get_inpt_files().send_keys(os.getcwd() + "/Example.pdf")
        time.sleep(3)
        print(self.get_check_emp())
        random_opt_sec = random.choice(self.get_check_emp())
        print(random_opt_sec)
        random_opt_sec.click()
        time.sleep(3)
        self.get_save_btn().click()
        time.sleep(5)

        if check_exito() is True:
            assert True
        else:
            print('Test Fallido.')
            assert False



