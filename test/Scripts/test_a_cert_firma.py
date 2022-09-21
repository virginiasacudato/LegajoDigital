from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.CertificadoFima import CertificadoFirma


class Test_CertFirma(WebDriverSetup):

    def test_a_alta(self):
        driver = self.driver
        cert_firma = CertificadoFirma(driver)
        cert_firma.alt_cert_raiz()

    def test_b_baja(self):
        driver = self.driver
        cert_firma = CertificadoFirma(driver)
        cert_firma.baja_cert_raiz()

    def test_c_mod(self):
        driver = self.driver
        cert_firma = CertificadoFirma(driver)
        cert_firma.alt_cert_raiz()


