from selenium.common.exceptions import NoSuchElementException
import time


def alt_cert_raiz(cert):

    def check_exito():
        try:
            msg = cert.get_msg_true().text
            print(msg)
            if msg == ' El proceso se realizó exitosamente! ':
                print('Coincide --> Operacion Exitosa')
        except NoSuchElementException:
            return False
        return True

    cert.get_cert_firma().click()
    cert.get_btn_raiz().click()
    time.sleep(3)
    cert.get_inp_pass().send_keys('admin')
    cert.get_new_cert().click()
    time.sleep(3)

    if check_exito() is True:
        assert True
    else:
        print('Operación con errores')
        assert False