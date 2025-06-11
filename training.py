
import subprocess
import time
import os
#TODO PG ADMIN  поставить себя
# на странице при переходе на отдельную страницу отобразить вывод команды df -h
# с помощью питоновского скрипта на странице по кнопке отобразить вывод команды df -h
# с помощью питоновского скрипта на странице по кнопке отобразить вывод команды watch df -h импортировать этот скрипт в отдельный файл views использовать os



result = subprocess.run("df -h", capture_output=True, text=True, shell=True)
print(result.stdout)

def clean_sh():
    return subprocess.run(['clear'], capture_output=True, text=True)
while True:
    # clear_screen()  # Очистить экран перед выводом
    # Выполнение команды df -h

    result = subprocess.run(['df', '-h'], capture_output=True, text=True, shell=True)
    clean_sh()
    print(result.stdout)  # Вывод результата
    time.sleep(3)  # Задержка перед следующим обновлением


