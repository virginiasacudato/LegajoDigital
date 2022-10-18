from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import os, shutil
import datetime
import time
import random
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'C:/Users/Maynar/Desktop/LegajoDigital/.env')
load_dotenv(dotenv_path)

# Environment Variables
USER_EMPLOY = os.getenv('USER_EMPLOY')
PASSWORD_EMPLOY = os.getenv('PASSWORD_EMPLOY')

for file in os.listdir('C:/Users/Maynar/Desktop/LegajoDigital'):
    if file.endswith(".pdf"):
        file_name = file
        path_file_name = os.path.join('C:/Users/Maynar/Desktop/LegajoDigital', file)

file_send = bool
employees_dni = ["45615684", "1648564968", "46461316", "54545615"]


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
        # Sign Files
        self.icon_sign = '//td[6]/a/img'
        self.pass_cert = '//*[@id="passwordCertificado"]'
        self.btn_firmar = '//*[@id="modalPassCertificadoRaiz"]/div[2]/div/div[3]/button[2]'
        self.status_table = '//*[@id="ListadoArchivos"]/tbody/tr[1]/td[3]'

        # -- EMPLEADO --
        # LogOut
        self.exit = '/html/body/main/header/div[2]/i'
        self.confirm = '//*[@id="1"]'
        # Login
        self.user = 'Usuario'
        self.password = 'Password'
        self.btn_ingresar = 'btnIngresar'
        # Section
        self.menu = '/html/body/main/aside/section/nav/ul/li[3]/div/label'
        self.rec_sueldo_emp = '/html/body/main/aside/section/nav/ul/li[3]/div/div/ul/li[2]/a'
        self.section = '/html/body/main/aside/section/nav/ul/li[3]/div/div/ul/li[2]/a'
        self.ver_y_firmar = '//*[@id="btnBorrar"]'
        self.btn_firmar_conforme = '//*[@id="modalFirmaRecibo"]/div[2]/div/div[3]/button[2]'
        self.btn_download = '//*[@id="11592"]/td[5]/a'
        self.status_rec_emp = '.td:nth-child(2)'

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

    # Sign Files

    def get_icon_sign_file(self):
        return self.driver.find_element(By.XPATH, self.icon_sign)

    def get_pass_cert(self):
        return self.driver.find_element(By.XPATH, self.pass_cert)

    def get_btn_firmar(self):
        return self.driver.find_element(By.XPATH, self.btn_firmar)

    def get_status_tables(self):
        return self.driver.find_elements(By.XPATH, self.status_table)

    # -- EMPLEADO --
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

    # Section RecibosDeSueldo
    def get_menu(self):
        return self.driver.find_element(By.XPATH, self.menu)

    def geT_rec_sueldo_emp(self):
        return self.driver.find_element(By.XPATH, self.rec_sueldo_emp)

    def get_rec_section(self):
        return self.driver.find_element(By.XPATH, self.section)

    def get_ver_y_firmar(self):
        return self.driver.find_element(By.XPATH, self.ver_y_firmar)

    def get_firmar_conforme(self):
        return self.driver.find_element(By.XPATH, self.btn_firmar_conforme)

    def get_btn_download(self):
        return self.driver.find_element(By.XPATH, self.btn_download)

    def get_status_rec_emp(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.status_rec_emp)


    # -- Actions --

    def upload_files(self):
        # Formatear archivo con la fecha actual
        date_now = datetime.date.today()
        ref_date = date_now.strftime("%d-%m-%Y")
        #print(ref_date)
        reformat_date = str(ref_date).replace('-', '')
        new_name_file_date = os.getcwd() + "/123456789-"+ reformat_date + "Recibo.pdf"
        #print(new_name_file_date)
        os.rename(path_file_name, new_name_file_date)
        time.sleep(10)
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
        #print("Los empleados iniciales son ", init_files)
        if file_name in init_files:
            new_name_file = os.getcwd() + "/" + random.choice(employees_dni) + "-22092022Recibo.pdf"
            os.rename(path_file_name, new_name_file)
            self.get_inpt_file().send_keys(path_file_name)
            time.sleep(4)
            #print('Encontrado!')
        else:
            self.get_inpt_file().send_keys(new_name_file_date)
            time.sleep(4)

        check_upload_files(final_files)
        #print("Los empleado finales son ", final_files)
        if init_files != final_files:
            assert True
        else:
            assert False

    def sign_file(self):

        self.get_recibosdesueldo().click()
        time.sleep(2)
        status_tables = self.get_status_tables()
        for status_table in status_tables:
            status_table_adm = status_table.text
        # print(name_status_table)

        if status_table_adm == "Firma pendiente":
            self.get_icon_sign_file().click()
            time.sleep(2)
            self.get_pass_cert().send_keys("admin")
            self.get_btn_firmar().click()
            time.sleep(5)
        else:
            print("ESTOY EN EL ELSE!")
            # En caso de que la firma no sea pendiente podria pasar al elemento de abajo y si este no lo tiene hacer lo mismo
            # Pero esto depende de que haya mas de un elemento en la tabla
            # Segun como esta creado los casos de prueba en este orden funciona y no deberia haber problemas para firmar un archivo
        time.sleep(5)

    def delete_files(self):
        self.get_recibosdesueldo().click()
        time.sleep(2)
        new_name_file = os.getcwd() + "/" + random.choice(employees_dni) + "-22092022Recibo.pdf"

        def check_table_empty():
            try:
                without_data = self.get_table_empty().text
                #print(without_data)
                if without_data == 'No hay datos para mostrar':
                    print("NO HAY DATOS!")
            except NoSuchElementException:
                #print("Soy false, estoy en el else")
                return False
            return True

        if check_table_empty() is True:
            # self.get_inpt_file().send_keys(os.getcwd() + "/123456789-22092022Recibo.pdf")
            self.get_inpt_file().send_keys(path_file_name)
            file_send = True
            self.get_trash_icon().click()
            time.sleep(4)
            self.get_btn_confirm().click()
            #print("file_send es true!!!")
            time.sleep(4)
        else:
            self.get_trash_icon().click()
            time.sleep(5)
            self.get_btn_confirm().click()
            time.sleep(5)
            file_send = False
            assert True
            #print("sali por el else, soy false!!!")

        if file_send is True:
            os.rename(path_file_name, new_name_file)
            #print("El nombre del archivo viejo es ", path_file_name)
            #print("El nombre del archivo nuevo es ", new_name_file)
            assert True
        else:
            assert True

    # -- EMPLEADO --
    # Firmar Empleado
    def firm_employ(self):

        self.geT_rec_sueldo_emp().click()

        #print(path_file_name)
        status_tables_emp = self.get_status_rec_emp().text
        print(status_tables_emp)
        if status_tables_emp == "Firmado por Usuario":
            print("Estoy en el if")
            self.get_icon_sign_file().click()
            time.sleep(2)
            self.get_ver_y_firmar().click()
            self.get_firmar_conforme().click()
            time.sleep(5)
        else:
            print("El archivo está firmado!")

        time.sleep(5)

    def access_employ(self):
        self.get_btn_exit().click()
        self.get_confirm().click()
        time.sleep(5)
        self.get_user().send_keys(USER_EMPLOY)
        self.get_password().send_keys(PASSWORD_EMPLOY)
        self.get_btn_ingresar().click()
        time.sleep(3)
        self.get_menu().click()
        self.get_rec_section().click()

    def download_emp(self):
        self.get_btn_download().click()
        while not os.path.exists(r"C:\Users\Maynar\Desktop\Test-Files"):
            time.sleep(2)

            # Check file
        if os.path.isfile(r"C:\Users\Maynar\Desktop\Test-Files\123456789-22092022Recibo.pdf"):
            print("File download is completed")
            assert True
        else:
            print("File download is not completed")
            assert False

        time.sleep(3)
        # Delete content folder
        folder = r"C:\Users\Maynar\Desktop\Test-Files"
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
