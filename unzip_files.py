import os
import zipfile

from clean_dirs import remove_files


def unzip_files():
    remove_files(r'extracted_data/*')
    file_list = ["building_res.txt", "real_acct.txt"]

    for root, subdir, filenames in os.walk('zipped_data'):
        for file in filenames:
            if file.split('.')[-1] == 'zip':
                zip_file_path = os.path.join(root, file)
                with zipfile.ZipFile(zip_file_path) as zip_obj:
                    list_of_file_names = zip_obj.namelist()

                    for file_name in list_of_file_names:
                        if file_name in file_list:
                            zip_obj.extract(file_name, 'extracted_data/')
