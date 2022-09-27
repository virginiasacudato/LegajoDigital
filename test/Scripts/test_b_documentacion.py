from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.Documentación import Documentacion
import time


class TestDocumentacion(WebDriverSetup):

    def test_a_alt_doc(self):
        driver = self.driver
        doc = Documentacion(driver)
        doc.upload_file()
    def test_b_baja_doc(self):
        driver = self.driver
        doc = Documentacion(driver)
        doc.del_file()

    def test_c_firmar_doc_adm(self):
        driver = self.driver
        doc = Documentacion(driver)
        doc.firmar_doc_subido()

    def test_d_firma_employ(self):
        driver = self.driver
        doc = Documentacion(driver)
        doc.access_employ()
        doc.firmar_doc_employ()
        time.sleep(3)

    def test_e_download_fl_emp(self):
        driver = self.driver
        doc = Documentacion(driver)
        doc.access_employ()
        doc.download_fl_emp()

    def test_d_check_download_file(self):
        driver = self.driver
        doc = Documentacion(driver)
        doc.check_download_file()
