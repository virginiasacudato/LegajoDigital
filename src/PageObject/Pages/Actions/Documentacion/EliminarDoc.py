import time



def del_file(doc):
    doc.get_documentacion().click()
    time.sleep(2)
    init_doc_emp_table = []
    final_doc_emp_table = []

    docs_emps = doc.get_docs_table()
    for doc_emp in docs_emps:
        docu_emp = doc_emp.text
        init_doc_emp_table.append(docu_emp)

    # print("Los empleados inicialmente con documentacion:", init_doc_emp_table)

    doc.get_trash_icon().click()
    time.sleep(5)
    doc.get_btn_confirm().click()
    time.sleep(3)

    docs_final_emp = doc.get_docs_table()

    for doc_final_emp in docs_final_emp:
        docu_final_emp = doc_final_emp.text
        final_doc_emp_table.append(docu_final_emp)

    # print("Los empleados finales luego de la eliminacion:", final_doc_emp_table)

    if init_doc_emp_table != final_doc_emp_table:
        # print("Hubo un elemento eliminado!!!")
        assert True
    else:
        # print("Algo fallo")
        assert False
