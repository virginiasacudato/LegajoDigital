from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class CertificadoFirma:

    # -- Locators --
    def __init__(self, driver):
        # Alta
        self.driver = driver
        # /html/body/main/aside/section/nav/ul/li[7]/div/div/ul/li[4]/a
        self.cert_firma = "//a[contains(text(),'Certificados Firma')]"
        self.btn_raiz = '//*[@id="CertificadosFirma"]/div[1]/button[2]'
        self.inp_pass = 'Password'
        self.new_cert = '//*[@id="modalNuevoCertificadoRaiz"]/div[2]/div/div[3]/button[2]'
        # self.msg_true = '//*[@id="modal-procesar-respuesta"]/div[2]/div/div[2]/label'
        self.msg_true = '//*[@id="modal-procesar-respuesta"]/div[2]/div/div[1]/h4'
        # Baja
        self.btn_del = '//*[@id="ListadoCertificados"]/tbody/tr/td[6]/a/i'
        self.btn_confirm = '.modal-dialog:nth-child(2) .btn:nth-child(2)'
        self.first_ele_tabl = '//*[@id="ListadoCertificados"]/tbody/tr[1]'
        self.table_empty = '.dataTables_empty'
        self.add_btn = '//*[@id="CertificadosFirma"]/div[1]/button[1]'
        self.create_cert_btn = '//*[@id="modalNuevoCertificado"]/div[2]/div/div[3]/button[2]'
        self.input_create_cert = '//*[@id="PasswordRoot"]'
        self.btn_entendido = '//*[@id="modal-procesar-respuesta"]/div[2]/div/div[3]/button'
        self.create_cert = '//*[@id="modalPassCertificadoRaiz"]/div[2]/div/div[3]/button[2]'
        self.emp_cert_firma = 'sorting_1'
        # xpath=//a[contains(text(),'Certificados Firma')]
        # //*[@id="modalPassCertificadoRaiz"]/div[2]/div/div[3]/button[2]
    # -- Get Elements --
    # Alta
    def get_cert_firma(self):
        return self.driver.find_element(By.XPATH, self.cert_firma)

    def get_btn_raiz(self):
        return self.driver.find_element(By.XPATH, self.btn_raiz)

    def get_inp_pass(self):
        return self.driver.find_element(By.ID, self.inp_pass)

    def get_new_cert(self):
        return self.driver.find_element(By.XPATH, self.new_cert)

    def get_msg_true(self):
        return self.driver.find_element(By.XPATH, self.msg_true)

    # Baja
    def get_btn_del(self):
        return self.driver.find_element(By.XPATH, self.btn_del)

    def get_btn_confirm(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.btn_confirm)

    def get_first_ele(self):
        return self.driver.find_element(By.XPATH, self.first_ele_tabl)

    def get_table_empty(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.table_empty)

    def get_add_btn(self):
        return self.driver.find_element(By.XPATH, self.add_btn)

    def get_crt_btn(self):
        return self.driver.find_element(By.XPATH, self.create_cert_btn)

    def get_inpt_pass_cert(self):
        return self.driver.find_element(By.XPATH, self.input_create_cert)

    def get_confirm_create_cert(self):
        return self.driver.find_element(By.XPATH, self.create_cert)

    def get_btn_entendido(self):
        return self.driver.find_element(By.XPATH, self.btn_entendido)

    def get_emp_cert_firma(self):
        return self.driver.find_elements(By.CLASS_NAME, self.emp_cert_firma)

    # -- Actions --

    # TEST SUITE  - ABM CERT.FIRMA

    def alt_cert_raiz(self):
        global pass_random
        pass_random = 'admin'
        def check_exito():
            try:
                msg = self.get_msg_true().text
                if msg == 'Operación Exitosa':
                    print('Coincide --> Operacion Exitosa')
            except NoSuchElementException:
                return False
            return True


        self.get_cert_firma().click()
        self.get_btn_raiz().click()
        time.sleep(3)
        self.get_inp_pass().send_keys(pass_random)
        self.get_new_cert().click()
        time.sleep(3)
        # self.driver.execute_script(WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.get_msg_true(), "Operación Exitosa")))
        if check_exito() is True:
            assert True
        else:
            print('Operación con errores')

    def baja_cert_raiz(self):
        self.get_cert_firma().click()

        init_names_emp_table = []
        final_names_emp_table = []

        # Almacenar los elementos iniciales de la tabla
        employees = self.get_emp_cert_firma()

        for employe in employees:
            emp_table = employe.text
            init_names_emp_table.append(emp_table)

        print("Los empleados inicialmente con certificado firma:", init_names_emp_table)

        # Chequeo de la tabla en caso de que este vacía
        def check_exists_by_xpath():
            try:
                without_data = self.get_table_empty().text
                if without_data == 'No hay datos para mostrar':
                    print("NO HAY DATOS!")
            except NoSuchElementException:
                return False
            return True
        # Condicion --> Tener previamente creado aunque sea un certificado
        if check_exists_by_xpath() is True:
            print("entre al if")
            # Crear Certificado
            self.get_add_btn().click()
            time.sleep(2)
            self.get_crt_btn().click()
            self.get_inpt_pass_cert().send_keys(pass_random)
            self.get_confirm_create_cert().click()
            time.sleep(2)
            self.get_btn_entendido().click()
            time.sleep(3)
            self.get_btn_del().click()
            self.get_btn_confirm().click()
            time.sleep(3)

        else:
            print("sali por el else")
            self.get_btn_del().click()
            time.sleep(5)
            self.get_btn_confirm().click()
            time.sleep(5)

        # Comprobacion de los elementos actuales de la tabla
        employees_finales = self.get_emp_cert_firma()

        for employe in employees_finales:
            emp_table = employe.text
            final_names_emp_table.append(emp_table)

        print('Empleados finales luego de la "eliminacion"', final_names_emp_table)



        # Capturar los td de la tabla
        # para ello crear un array inicial y un array final
        # comparar y en caso de que se elimine uno, assert.




