import os
import shutil  # import os module


def cur_package_path():
    return str(__file__)[:str(__file__).rfind('/') + 1]


def safe_mkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def safe_mkfile(name, content):
    if not os.path.isfile(name):
        f = open(name, 'w')
        f.write(content)
        f.close()


files_path = cur_package_path() + '/files'

safe_mkdir(files_path + '/folder_zip')  # Create my_zip.zip file in current work directory
zip_dir_path = files_path + '/folder_zip'

for filename in range(3):  # Create files with data in current folder
    safe_mkfile(zip_dir_path + '/file_%s' % filename, 'some data')

shutil.make_archive("my_zip", "zip", root_dir=".",
                    base_dir="./files/folder_zip")  # Create my_zip.zip file in current work directory

shutil.copy("my_zip.zip", "../my_zip.zip")  # Copy archive into folder above
shutil.rmtree(zip_dir_path)  # Remove folder_zip
input()  # Wait for user input and check the data here
shutil.unpack_archive("../my_zip.zip")  # Unpack files into folder_zip
os.remove("my_zip.zip")  # Remove archive from current folder
os.remove("../my_zip.zip")  # Remove archive from folder above
print(shutil.disk_usage("."))  # Print disk Usage of current folder
