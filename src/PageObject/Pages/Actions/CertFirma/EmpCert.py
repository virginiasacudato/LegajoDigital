import time


def add_cert_to_employees(cert):
    cert.get_cert_firma().click()
    cert.get_btn_add_cert().click()
    time.sleep(3)
    cert.get_btn_confirm_add().click()
    cert.get_inpt_pass_add_cert().send_keys('admin')
    cert.get_firmar_certificado().click()
    time.sleep(6)