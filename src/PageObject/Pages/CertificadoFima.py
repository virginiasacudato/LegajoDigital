from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class CertificadoFirma:

    # -- Locators --
    def __init__(self, driver):
        # Alta
        self.driver = driver
        self.cert_firma = '/html/body/main/aside/section/nav/ul/li[7]/div/div/ul/li[4]/a'
        self.btn_raiz = '//*[@id="CertificadosFirma"]/div[1]/button[2]'
        self.inp_pass = 'Password'
        self.new_cert = '//*[@id="modalNuevoCertificadoRaiz"]/div[2]/div/div[3]/button[2]'
        #self.msg_true = '//*[@id="modal-procesar-respuesta"]/div[2]/div/div[2]/label'
        self.msg_true = '//*[@id="modal-procesar-respuesta"]/div[2]/div/div[1]/h4'
        # Baja
        self.btn_del = '//*[@id="ListadoCertificados"]/tbody/tr/td[6]/a/i'
        self.btn_confirm = '//*[@id="modal-danger-delete-certificado"]/div[2]/div/div[3]/button[2]'
        self.first_ele_tabl = '//*[@id="ListadoCertificados"]/tbody/tr[1]'
        self.add_btn = '//*[@id="CertificadosFirma"]/div[1]/button[1]'
        self.create_cert_btn = '//*[@id="modalNuevoCertificado"]/div[2]/div/div[3]/button[2]'
        self.input_create_cert = '//*[@id="PasswordRoot"]'
        self.btn_entendido = '//*[@id="modal-procesar-respuesta"]/div[2]/div/div[3]/button'


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
        return self.driver.find_elements(By.XPATH, self.msg_true)

    # Baja
    def get_btn_del(self):
        return self.driver.find_element(By.XPATH, self.btn_del)

    def get_btn_confirm(self):
        return self.driver.find_element(By.XPATH, self.btn_confirm)

    def get_first_ele(self):
        return self.driver.find_element(By.XPATH, self.first_ele_tabl)

    def get_add_btn(self):
        return self.driver.find_element(By.XPATH, self.add_btn)

    def get_crt_btn(self):
        return self.driver.find_element(By.XPATH, self.create_cert_btn)

    def get_inpt_pass_cert(self):
        return self.driver.find_element(By.XPATH, self.input_create_cert)

    def get_btn_entendido(self):
        return self.driver.find_element(By.XPATH, self.btn_entendido)

    # -- Actions --

    # TEST SUITE  - ABM CERT.FIRMA

    def alt_cert_raiz(self):
        global pass_random
        pass_random = 'admin'
        self.get_cert_firma().click()
        self.get_btn_raiz().click()
        time.sleep(3)
        self.get_inp_pass().send_keys(pass_random)
        self.get_new_cert().click()
        time.sleep(3)
        self.driver.execute_script(WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.get_msg_true(), "Operación Exitosa")))

    def baja_cert_raiz(self):
        def check_exists_by_xpath():
            try:
                self.get_first_ele()
            except NoSuchElementException:
                return False
            return True
        # Condicion --> Tener previamente creado aunque sea un certificado

        if check_exists_by_xpath() is True:
            self.get_btn_del().click()
            self.get_btn_confirm().click()
        else:
            # Crear Certificado
            self.get_add_btn().click()
            self.get_crt_btn().click()
            self.get_inpt_pass_cert().send_keys(pass_random)
            self.get_btn_entendido().click()
            self.get_btn_del().click()
            self.get_btn_confirm().click()







