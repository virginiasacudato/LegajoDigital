# Import Web Driver
from src.TestBase.WebDriverSetup import WebDriverSetup

# Import Elements
from src.PageObject.Pages.Elements.Documentación import Documentacion

# Import Actions
from src.PageObject.Pages.Actions.Documentacion.FirmarDocAdm import *
from src.PageObject.Pages.Actions.Documentacion.Empleado.Access import *
from src.PageObject.Pages.Actions.Documentacion.Empleado.FirmarDocEmp import *
from src.PageObject.Pages.Actions.Documentacion.Empleado.DescargarDocEmp import *
from src.PageObject.Pages.Actions.Documentacion.DescargarDoc import *

# Time
import time


class TestDocumentacion(WebDriverSetup):

    def test_a_firmar_doc_adm(self):
        driver = self.driver
        doc = Documentacion(driver)
        firmar_doc_subido(doc)

    def test_b_firma_employ(self):
        driver = self.driver
        doc = Documentacion(driver)
        access_employ(doc)
        firmar_doc_employ(doc)
        time.sleep(3)

    def test_c_download_fl_emp(self):
        driver = self.driver
        doc = Documentacion(driver)
        access_employ(doc)
        download_fl_emp(doc)

    def test_d_check_download_file(self):
        driver = self.driver
        doc = Documentacion(driver)
        check_download_file(doc)
        time.sleep(2)

    def test_e_baja_doc(self):
        driver = self.driver
        doc = Documentacion(driver)
        doc.del_file()
