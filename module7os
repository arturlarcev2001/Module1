import os


import os
import time

directory = 'D:\\pythonProjects' 
f = open("d.txt", "w+")

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(root, file)
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(filepath)
    file_line = "filepath:{}\n filetime:{}\n formatted_time:{}\n filesize:{}\n parent_dir:{}\n\n".format(filepath, filetime, formatted_time, filesize, parent_dir)
    f.write(file_line)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

f.close()
