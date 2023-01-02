from selenium.webdriver.common.by import By


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
        self.msg_true = '//*[@id="modal-procesar-respuesta"]/div/div/div/label'
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
        # Add cert raiz to employees
        self.btn_add_cert = '//*[@id="CertificadosFirma"]/div[1]/button[1]'
        self.btn_confirm_add = '//*[@id="modalNuevoCertificado"]/div[2]/div/div[3]/button[2]'
        self.inpt_pass_add_cert = '//*[@id="PasswordRoot"]'
        self.firmar_cert = '//*[@id="modalPassCertificadoRaiz"]/div[2]/div/div[3]/button[2]'

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

    # Asignar Cert. Firma a empleados
    def get_btn_add_cert(self):
        return self.driver.find_element(By.XPATH, self.btn_add_cert)

    def get_btn_confirm_add(self):
        return self.driver.find_element(By.XPATH, self.btn_confirm_add)

    def get_inpt_pass_add_cert(self):
        return self.driver.find_element(By.XPATH, self.inpt_pass_add_cert)

    def get_firmar_certificado(self):
        return self.driver.find_element(By.XPATH, self.firmar_cert)