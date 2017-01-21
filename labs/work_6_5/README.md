##Laboratory Work 6.5.

Create a module with name my_shutil.py with next code implementation:

* Create “folder_zip’ in current working directory
* Create 3 files with an types of data in “folder_zip”
* Archive “folder_zip” contents into one zip file with name “my_zip”
* Copy “my_zip” into one folder above current
* Remove folder “folder_zip” from disk
* Add user prompt for checking folder state
* Unpack archive in current folder
* Print disk usage of folder were archive were copied

####Here is the solution code:

*solution_6_5.py*

```python
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
```
