import os
import platform

# current working directory
cwd = os.path.abspath(".")

# print computer name, processor architecture
print('computer name:', os.uname()[1])

print('processor architecture:', platform.processor())


# print current work directory
print('\n\t\tcurrent work directory:\n', os.getcwd())


# change work directory to "C:"
os.chdir('/home')
print('\n\t\tcurrent work directory:\n', os.getcwd())


# print list of directories
print('\nlist of directories ({}):'.format(os.getcwd()),
      [directory for directory in os.listdir(".") if os.path.isdir(directory)])


# print list of files
os.chdir('/')
print('\nlist of files ({}):'.format(os.getcwd()),
      [file for file in os.listdir(".") if os.path.isfile(file)])


# for files check is it link or not
os.chdir('/bin')
print('\nfilter of links ({}):'.format(os.getcwd())),
for file in os.listdir("."):
    if os.path.islink(file):
        print('\t\t', file, '-----> is link!')
    else:
        print('\t\t', file)


# Back to initial work directory
os.chdir(cwd)

# Create “Temp” folder
print('\n\'Temp\' directory created!\n')
os.mkdir('Temp')

# Delete “Temp” folder
print('\n\'Temp\' directory deleted!\n')
os.rmdir('Temp')
