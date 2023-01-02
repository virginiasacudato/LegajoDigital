import time


def firmar_doc_employ(doc):
    doc.get_firmar_btn().click()
    doc.get_firmar_conforme().click()
    time.sleep(2)
    status_doc = doc.get_status_table().text
    #print(status_doc)
    if status_doc == "Firmado conforme por Empleado":
        print("Firma realizada")
        assert True
    else:
        assert False

