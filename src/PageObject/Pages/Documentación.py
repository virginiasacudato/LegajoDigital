from selenium.webdriver.common.by import By
import os, shutil
import time
import random
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), 'C:/Users/Maynar/Desktop/LegajoDigital/.env')
load_dotenv(dotenv_path)

# Environment Variables
USER_EMPLOY = os.getenv('USER_EMPLOY')
PASSWORD_EMPLOY = os.getenv('PASSWORD_EMPLOY')

for file in os.listdir('C:/Users/Maynar/Desktop/LegajoDigital/docExample'):
    if file.endswith(".pdf"):
        file_name = file
        path_file_name = os.path.join('C:\\Users\\Maynar\\Desktop\\LegajoDigital\\docExample', file)




# random_names_files = ["Example10", "Example12", "Example13", "Example14", "Example15"]


class Documentacion:

    # -- Locators --
    def __init__(self, driver):
        self.driver = driver
        # Button Menu
        self.documentacion = '/html/body/main/aside/section/nav/ul/li[7]/div/div/ul/li[2]/a'
        # Upload files
        self.inpt_file = '//*[@id="divRecuperarArchivos"]/div/input'
        self.check_emp = '//*[@id="tableBodyEmpleados"]/tr[3]/td/div'
        self.btn_save = 'firmar-y-guardar'
        self.msg_exitoso = '//*[@id="modal-procesar-respuesta"]/div[2]/div/div[1]/h4'
        # Delete Files
        self.trash = '//*[@id="ListadoArchivos"]/tbody/tr[1]/td[8]/a/i'
        self.btn_confirm = '//*[@id="modal-danger-delete-selected-recibos"]/div[2]/div/div[3]/button[2]'
        self.doc_table = 'sorting_1'
        # Firmar File
        self.firma_req = '//*[@id="modalSeleccionarEmpleados"]/div[2]/div/div[2]/div[3]/label'
        self.pass_cert_raiz = 'PasswordCertificado'
        self.emp_especifico = ".even:nth-child(8) label"
        # Dowload File
        self.btn_down_pdf = '//*[@id="ListadoArchivos_wrapper"]/div[1]/button[2]'

        # EMPLEADO
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
        self.name_doc = '//*[@id="tablaArchivo"]/tbody/tr[1]/td[1]'
        # Firmar Doc
        self.firmar_btn = '//*[@id="btnFirmarDocumentacion"]'
        self.firmar_conforme = '//*[@id="modalFirmaDocumentos"]/div[2]/div/div[3]/button[2]'
        self.status = '//*[@id="tablaArchivo"]/tbody/tr/td[3]'
        self.download_file = '//*[@id="tablaArchivo"]/tbody/tr/td[5]/a'

    # -- Get Elements --
    def get_documentacion(self):
        return self.driver.find_element(By.XPATH, self.documentacion)

    def get_inpt_files(self):
        return self.driver.find_element(By.XPATH, self.inpt_file)

    def get_check_emp(self):
        return self.driver.find_elements(By.XPATH, self.check_emp)

    def get_emp_especifico(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.emp_especifico)

    def get_save_btn(self):
        return self.driver.find_element(By.ID, self.btn_save)

    def get_msg_exitoso(self):
        return self.driver.find_element(By.XPATH, self.msg_exitoso)

    # Delete file
    def get_trash_icon(self):
        return self.driver.find_element(By.XPATH, self.trash)

    def get_btn_confirm(self):
        return self.driver.find_element(By.XPATH, self.btn_confirm)

    def get_docs_table(self):
        return self.driver.find_elements(By.CLASS_NAME, self.doc_table)

    # Firmar file

    def get_firma_req(self):
        return self.driver.find_element(By.XPATH, self.firma_req)

    def get_pass_cert_raiz(self):
        return self.driver.find_element(By.ID, self.pass_cert_raiz)

    # Download File

    def get_btn_down_file(self):
        return self.driver.find_element(By.XPATH, self.btn_down_pdf)

    # --- EMPLEADO ---

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

    def get_firmar_conforme(self):
        return self.driver.find_element(By.XPATH, self.firmar_conforme)

    def get_status_table(self):
        return self.driver.find_element(By.XPATH, self.status)

    def get_dowload_file(self):
        return self.driver.find_element(By.XPATH, self.download_file)

    def get_name_doc_file(self):
        return self.driver.find_element(By.XPATH, self.name_doc)

    # -- Actions --


    def firmar_doc_employ(self):
        self.get_firmar_btn().click()
        self.get_firmar_conforme().click()
        time.sleep(2)
        status_doc = self.get_status_table().text
        #print(status_doc)
        if status_doc == "Firmado conforme por Empleado":
            #print("Firma realizada")
            assert True
        else:
            assert False

    def del_file(self):
        self.get_documentacion().click()
        time.sleep(2)
        init_doc_emp_table = []
        final_doc_emp_table = []

        docs_emps = self.get_docs_table()
        for doc_emp in docs_emps:
            docu_emp = doc_emp.text
            init_doc_emp_table.append(docu_emp)

        #print("Los empleados inicialmente con documentacion:", init_doc_emp_table)

        self.get_trash_icon().click()
        time.sleep(5)
        self.get_btn_confirm().click()
        time.sleep(3)

        docs_final_emp = self.get_docs_table()

        for doc_final_emp in docs_final_emp:
            docu_final_emp = doc_final_emp.text
            final_doc_emp_table.append(docu_final_emp)

        #print("Los empleados finales luego de la eliminacion:", final_doc_emp_table)

        if init_doc_emp_table != final_doc_emp_table:
            #print("Hubo un elemento eliminado!!!")
            assert True
        else:
            #print("Algo fallo")
            assert False

    def firmar_doc_subido(self):
        random_names_files = random.randint(1, 200)
        self.get_documentacion().click()

        def check_upload_files(array):
            table_files = self.get_docs_table()
            for table_file in table_files:
                table_file_name = table_file.text
                array.append(table_file_name)

        init_files = []
        final_files = []

        time.sleep(2)
        check_upload_files(init_files)
        #print("Los empleados iniciales son ", init_files)

        if file_name in init_files:
            new_name_file = os.getcwd() + '\\docExample\\' + "Example" + str(random_names_files) + ".pdf"
            os.rename(path_file_name, new_name_file)
            time.sleep(6)
            self.get_inpt_files().send_keys(new_name_file)
            time.sleep(4)
            #print('Encontrado!')
        else:
            new_name_file = os.getcwd() + '\\docExample\\' + "Example" + str(random_names_files) + ".pdf"
            os.rename(path_file_name, new_name_file)
            time.sleep(10)
            self.get_inpt_files().send_keys(new_name_file)
            time.sleep(4)

        time.sleep(5)
        self.get_emp_especifico().click()  # Click a empleado especifico
        time.sleep(3)
        self.get_firma_req().click()
        time.sleep(2)
        self.get_pass_cert_raiz().send_keys('admin')
        self.get_save_btn().click()
        time.sleep(4)

        check_upload_files(final_files)
        #print("Los empleado finales son ", final_files)

        if init_files != final_files:
            assert True
        else:
            assert False

    def check_download_file(self):

        self.get_documentacion().click()
        self.get_btn_down_file().click()
        time.sleep(6)

        while not os.path.exists(r"C:\Users\Maynar\Desktop\Test-Files"):
            time.sleep(2)

        # Check file
        if os.path.isfile(r"C:\Users\Maynar\Desktop\Test-Files\Documentación.pdf"):
            #print("File download is completed")
            assert True
        else:
            #print("File download is not completed")
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

    def download_fl_emp(self):
        self.get_dowload_file().click()
        get_name_doc = self.get_name_doc_file().text
        print(get_name_doc)
        time.sleep(4)

        while not os.path.exists(r"C:\Users\Maynar\Desktop\Test-Files"):
            time.sleep(2)

        path_is_file = r'C:\\Users\\Maynar\\Desktop\\Test-Files\\' + get_name_doc
        # Check file
        if os.path.isfile(path_is_file):
            #print("File download is completed")
            assert True
        else:
            #print("File download is not completed")
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

    # EMPLEADO

    def access_employ(self):
        self.get_btn_exit().click()
        self.get_confirm().click()
        time.sleep(5)
        self.get_user().send_keys(USER_EMPLOY)
        self.get_password().send_keys(PASSWORD_EMPLOY)
        self.get_btn_ingresar().click()
        time.sleep(3)
        self.get_doc_section().click()
        self.get_doc().click()
