from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.Documentación import Documentacion


class TestDocumentacion(WebDriverSetup):

    def test_a_alt_doc(self):
        driver = self.driver
        doc = Documentacion(driver)
        doc.upload_file()

    def test_b_baja_doc(self):
        driver = self.driver
        doc = Documentacion(driver)
        doc.del_file()