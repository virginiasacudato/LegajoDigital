import time
import os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '/.env')
load_dotenv(dotenv_path)

# Environment Variables
USER_EMPLOY = os.getenv('USER_EMPLOY')
PASSWORD_EMPLOY = os.getenv('PASSWORD_EMPLOY')


def access_employ(doc):
    doc.get_btn_exit().click()
    doc.get_confirm().click()
    time.sleep(5)
    doc.get_user().send_keys(USER_EMPLOY)
    doc.get_password().send_keys(PASSWORD_EMPLOY)
    doc.get_btn_ingresar().click()
    time.sleep(3)
    doc.get_doc_section().click()
    doc.get_doc().click()