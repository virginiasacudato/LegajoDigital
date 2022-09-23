from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os
import time
import random
import re

for file in os.listdir('C:/Users/Maynar/Desktop/LegajoDigital'):
    if file.endswith(".pdf"):
        file_name = file
        path_file_name = os.path.join('C:/Users/Maynar/Desktop/LegajoDigital', file)


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
        # Check Upload Files
        self.files_table = 'sorting_1'

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

    # Check Upload Files

    def get_files_table(self):
        return self.driver.find_elements(By.CLASS_NAME, self.files_table)

    # -- Actions --

    def upload_files(self):
        def check_upload_files(array):
            table_files = self.get_files_table()
            for table_file in table_files:
                table_file_name = table_file.text
                array.append(table_file_name)

        init_files = []
        final_files = []

        self.get_recibosdesueldo().click()
        time.sleep(4)
        check_upload_files(init_files)
        print("Los empleados iniciales son ", init_files)
        if file_name in init_files: print('Encontrado!')

        self.get_inpt_file().send_keys(path_file_name)
        time.sleep(4)
        check_upload_files(final_files)
        print("Los empleado finales son ", final_files)
        if init_files == final_files:
            assert True
        else:
            assert False

    def delete_files(self):

        file_send = bool
        employees_dni = ["45615684", "1648564968", "46461316", "54545615"]
        self.get_recibosdesueldo().click()
        time.sleep(2)
        new_name_file = os.getcwd() + "/" + random.choice(employees_dni) + "-22092022Recibo.pdf"

        def check_table_empty():
            try:
                without_data = self.get_table_empty().text
                print(without_data)
                if without_data == 'No hay datos para mostrar':
                    print("NO HAY DATOS!")
            except NoSuchElementException:
                print("Soy false, estoy en el else")
                return False
            return True

        if check_table_empty() is True:
            # self.get_inpt_file().send_keys(os.getcwd() + "/123456789-22092022Recibo.pdf")
            self.get_inpt_file().send_keys(path_file_name)
            file_send = True
            self.get_trash_icon().click()
            time.sleep(4)
            self.get_btn_confirm().click()
            print("file_send es true!!!")
            time.sleep(4)
        else:
            self.get_trash_icon().click()
            time.sleep(5)
            self.get_btn_confirm().click()
            time.sleep(5)
            file_send = False
            assert True
            print("sali por el else, soy false!!!")

        if file_send is True:
            os.rename(path_file_name, new_name_file)
            print("El nombre del archivo viejo es ", path_file_name)
            print("El nombre del archivo nuevo es ", new_name_file)
            assert True
        else:
            AssertionError
