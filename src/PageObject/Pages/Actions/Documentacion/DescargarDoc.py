import time
import shutil
import os


def check_download_file(doc):
    doc.get_documentacion().click()
    doc.get_btn_down_file().click()
    time.sleep(6)

    while not os.path.exists(r"C:\Users\Maynar\Desktop\Test-Files"):
        time.sleep(2)

    # Check file
    if os.path.isfile(r"C:\Users\Maynar\Desktop\Test-Files\Documentación.pdf"):
        # print("File download is completed")
        assert True
    else:
        # print("File download is not completed")
        assert False

    time.sleep(3)
    # Delete content folder
    folder = r"C:\Users\Maynar\Desktop\Test-Files"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))