import time
import os, shutil

def download_fl_emp(doc):
    doc.get_dowload_file().click()
    get_name_doc = doc.get_name_doc_file().text
    print(get_name_doc)
    time.sleep(4)

    while not os.path.exists(r"C:\Users\Maynar\Desktop\Test-Files"):
        time.sleep(2)

    path_is_file = r'C:\\Users\\Maynar\\Desktop\\Test-Files\\' + get_name_doc
    # Check file
    if os.path.isfile(path_is_file):
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