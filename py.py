import os
import re
import getpass
import colorama
from colorama import Fore, Back, Style
import time

colorama.init()
username = getpass.getuser()

try:
	direct1 = input(str("Введите директорию: "))
	direct = os.listdir(direct1)
except FileNotFoundError:
	print(Fore.RED, "[+] Не правильно указан путь, попробуйте заново!")
	time.sleep(3)
	exit()

for i in range(len(direct)):
	path = f"{direct1}{direct[i]}"
	os.chdir(path)
	with open("UserInformation.txt", "r", encoding='utf-8') as file:
		lines = file.readlines()
		ip = lines[12]
		ip1 = str(ip.replace(ip[0], "").replace(ip[1], "Айпи"))
		user = lines[14]
		user1 = str(user.replace(user[:8], "Юзер"))
		count = lines[15]
		count1 = str(count.replace(count[:7], "Страна"))
		zip1 = lines[16]
		zip2 = str(zip1.replace(zip1[:8], "ZIP-код"))
		loc = lines[17]
		loc1 = str(loc.replace(loc[:8], "Локация"))
		hwid = lines[18]
		lang = lines[19]
		lang1 = str(lang.replace(lang[:16], "Язык"))
		screen = lines[20]
		screen1 = str(screen.replace(screen[:10], "Разрешение экрана").replace("{", "").replace("}", ""))
		time2 = lines[21]
		time1= str(time2.replace(time2[:8], "Время"))
		oper = lines[22]
		oper1 = str(oper.replace(oper[:16], "Операционная система"))
		LOGS_DATE = lines[25]
		LOGS_DATE1 = str(LOGS_DATE.replace(LOGS_DATE[:9], "Дата лога:"))

	with open(f"C:/Users/{username}/Desktop/CheckLogs.txt", "a", encoding = "utf-8") as file:
		file.write(f"Лог №{i}\n---------------------------\n{ip1}{user1}{count1}{zip2}{loc1}{hwid}{lang1}{screen1}{time1}{oper1}\n{LOGS_DATE1}---------------------------\n\n")
		file.close()

print(Fore.GREEN, "[+] Логи установлены...")
time.sleep(3)
print(Fore.GREEN, "[+] Сортировка логов...")
time.sleep(3)
print(Fore.GREEN, "[+] Логи успешно сортированы и скачаны!")
time.sleep(5)
