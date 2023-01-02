# Import Web Driver
from src.TestBase.WebDriverSetup import WebDriverSetup

# Import Elements
from src.PageObject.Pages.Elements import CertificadoFima

# Import Actions
from src.PageObject.Pages.Actions.CertFirma.CrearCert import *
from src.PageObject.Pages.Actions.CertFirma.BajaCert import *
from src.PageObject.Pages.Actions.CertFirma.EmpCert import *


class Test_CertFirma(WebDriverSetup):

    def test_a_alta(self):
        driver = self.driver
        cert = CertificadoFima(driver)
        alt_cert_raiz(cert)
    def test_b_baja(self):
        driver = self.driver
        cert = CertificadoFima(driver)
        baja_cert_raiz(cert)
    def test_c_mod(self):
        driver = self.driver
        cert = CertificadoFima(driver)
        alt_cert_raiz(cert)

    def test_d_add_cert_to_employees(self):
        driver = self.driver
        cert = CertificadoFima(driver)
        add_cert_to_employees(cert)


