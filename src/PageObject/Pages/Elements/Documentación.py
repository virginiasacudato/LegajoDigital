from selenium.webdriver.common.by import By


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
        self.exit = '//*[@id="salir"]'
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