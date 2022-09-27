from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.RecibosDeSueldo import RecibosDeSueldo


class TestReciboDeSueldo(WebDriverSetup):

    def test_a_upload_rec(self):
        driver = self.driver
        rec_s = RecibosDeSueldo(driver)
        rec_s.upload_files()

    def test_b_firmar_rec(self):
        driver = self.driver
        rec_s = RecibosDeSueldo(driver)
        rec_s.sign_file()

    def test_c_firmar_emp(self):
        driver = self.driver
        rec_s = RecibosDeSueldo(driver)
        rec_s.firm_employ()
        rec_s.access_employ()
        rec_s.ver_y_firma()

    def test_d_dowload_fs_emp(self):
        driver = self.driver
        rec_s = RecibosDeSueldo(driver)
        rec_s.access_employ()


    def test_d_del_rec(self):
        driver = self.driver
        rec_s = RecibosDeSueldo(driver)
        rec_s.delete_files()
