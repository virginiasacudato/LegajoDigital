import time
import random
import os


for file in os.listdir(r'/docExample'):
    if file.endswith(".pdf"):
        file_name = file
        path_file_name = os.path.join(r'/docExample', file)


for file in os.listdir('/docExample'):
    if file.endswith(".pdf"):
        file_name = file
        path_file_name = os.path.join('/docExample', file)


def firmar_doc_subido(doc):
    random_names_files = random.randint(1, 200)
    doc.get_documentacion().click()

    def check_upload_files(array):
        table_files = doc.get_docs_table()
        for table_file in table_files:
            table_file_name = table_file.text
            array.append(table_file_name)

    init_files = []
    final_files = []

    time.sleep(2)
    check_upload_files(init_files)
    # print("Los empleados iniciales son ", init_files)

    if file_name in init_files:
        new_name_file = os.getcwd() + '\\docExample\\' + "Example" + str(random_names_files) + ".pdf"
        os.rename(path_file_name, new_name_file)
        time.sleep(6)
        doc.get_inpt_files().send_keys(new_name_file)
        time.sleep(4)
        # print('Encontrado!')
    else:
        new_name_file = os.getcwd() + '\\docExample\\' + "Example" + str(random_names_files) + ".pdf"
        os.rename(path_file_name, new_name_file)
        time.sleep(10)
        doc.get_inpt_files().send_keys(new_name_file)
        time.sleep(4)

    time.sleep(5)
    doc.get_emp_especifico().click()  # Click a empleado especifico
    time.sleep(3)
    doc.get_firma_req().click()
    time.sleep(2)
    doc.get_pass_cert_raiz().send_keys('admin')
    doc.get_save_btn().click()
    time.sleep(4)

    check_upload_files(final_files)
    # print("Los empleado finales son ", final_files)

    if init_files != final_files:
        assert True
    else:
        assert False