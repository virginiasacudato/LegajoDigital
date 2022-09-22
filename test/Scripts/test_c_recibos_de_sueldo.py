from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.RecibosDeSueldo import RecibosDeSueldo


class TestReciboDeSueldo(WebDriverSetup):

    #def test_a_upload_rec(self):
    #    driver = self.driver
    #    rec_s = RecibosDeSueldo(driver)
    #    rec_s.upload_files()

    def test_b_del_rec(self):
        driver = self.driver
        rec_s = RecibosDeSueldo(driver)
        rec_s.delete_files()


