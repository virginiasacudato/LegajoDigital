from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time
import random


class RecibosDeSueldo:

    # -- Locators --
    def __init__(self, driver):
        self.driver = driver
        # Button Menu
        self.recibosdesueldo = "//a[contains(text(),'Recibos de sueldo')]"
        # Upload File
        self.inpt_file = '//*[@id="divRecuperarArchivos"]/div/input'
        # Delete Files
        self.trash_icon = '//*[@id="ListadoArchivos"]/tbody/tr/td[7]/a/i'
        self.btn_confirm = '//*[@id="modal-danger-delete-selected-recibos"]/div[2]/div/div[3]/button[2]'
        self.table_empty = 'dataTables_empty'

    # -- Get Elements --

    def get_recibosdesueldo(self):
        return self.driver.find_element(By.XPATH, self.recibosdesueldo)

    # Upload Files

    def get_inpt_file(self):
        return self.driver.find_element(By.XPATH, self.inpt_file)

    # Delete Files

    def get_trash_icon(self):
        return self.driver.find_element(By.XPATH, self.trash_icon)

    def get_btn_confirm(self):
        return self.driver.find_element(By.XPATH, self.btn_confirm)

    def get_table_empty(self):
        return self.driver.find_element(By.CLASS_NAME, self.table_empty)

    # -- Actions --

    def upload_files(self):
        #def check_exito():
        #    try:
        #        msg = self.get_msg_exitoso().text
        #        if msg == 'Operación Exitosa':
        #            print('Coincide --> Operación Exitosa')
        #    except NoSuchElementException:
        #        return False
        #    return True

        self.get_recibosdesueldo().click()
        time.sleep(4)

        self.get_inpt_file().send_keys(os.getcwd() + "/123456789-22092022Recibo.pdf")
        time.sleep(4)

        #if check_exito() is True:
        #    assert True
        #else:
        #    print('Test Fallido.')
        #    assert False

    def delete_files(self):
        file_send = bool
        employees_dni = ["45615684", "1648564968", "46461316", "54545615"]
        self.get_recibosdesueldo().click()
        time.sleep(2)

        def check_exists_by_xpath():
            try:
                without_data = self.get_table_empty().text
                print(without_data)
                if without_data == 'No hay datos para mostrar':
                    print("NO HAY DATOS!")
            except NoSuchElementException:
                print("Soy false, estoy en el else")
                return False
            return True

        if check_exists_by_xpath() is True:
            self.get_inpt_file().send_keys(os.getcwd() + "/123456789-22092022Recibo.pdf")
            file_send = True
            print("file_send es true!!!")
            time.sleep(4)
        else:
            self.get_trash_icon().click()
            time.sleep(5)
            self.get_btn_confirm().click()
            time.sleep(5)
            file_send = False
            print("sali por el else, soy false!!!")

        if file_send is True:
            new_name_file = os.rename(os.getcwd() + "/123456789-22092022Recibo.pdf", os.getcwd() +"/"+random.choice(employees_dni)+ "-22092022Recibo.pdf")
            print(new_name_file)

