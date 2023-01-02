from selenium.common.exceptions import NoSuchElementException
import time


def baja_cert_raiz(cert):
    cert.get_cert_firma().click()

    init_names_emp_table = []
    final_names_emp_table = []

    # Almacenar los elementos iniciales de la tabla
    employees = cert.get_emp_cert_firma()

    for employe in employees:
        emp_table = employe.text
        init_names_emp_table.append(emp_table)

    print("Los empleados inicialmente con certificado firma:", init_names_emp_table)

    # Chequeo de la tabla en caso de que este vacía
    def check_exists_by_xpath():
        try:
            without_data = cert.get_table_empty().text
            if without_data == 'No hay datos para mostrar':
                print("NO HAY DATOS!")
        except NoSuchElementException:
            return False
        return True

    # Condicion --> Tener previamente creado aunque sea un certificado
    if check_exists_by_xpath() is True:
        print("entre al if")
        # Crear Certificado
        cert.get_add_btn().click()
        time.sleep(2)
        cert.get_crt_btn().click()
        cert.get_inpt_pass_cert().send_keys('admin')
        cert.get_confirm_create_cert().click()
        time.sleep(2)
        cert.get_btn_entendido().click()
        time.sleep(3)
        cert.get_btn_del().click()
        cert.get_btn_confirm().click()
        time.sleep(3)

    else:
        print("sali por el else")
        cert.get_btn_del().click()
        time.sleep(5)
        cert.get_btn_confirm().click()
        time.sleep(5)

    # Comprobacion de los elementos actuales de la tabla
    employees_finales = cert.get_emp_cert_firma()

    for employe in employees_finales:
        emp_table = employe.text
        final_names_emp_table.append(emp_table)

    print('Empleados finales luego de la "eliminacion"', final_names_emp_table)

    if init_names_emp_table != final_names_emp_table:
        print("Hubo un elemento eliminado!!!")
        assert True
    else:
        print("Algo fallo")
        assert False