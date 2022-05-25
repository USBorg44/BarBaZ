#!/usr/bin/env python
#setup

import os
import time as T

def clean():
	os.system('clear')
	if os.name == 'nt':
		os.system('cls')

def main():
	a = os.system

	b_1 = 'sudo apt-get update'
	b_2 = 'sudo apt-get install aircrack-ng'
	b_3 = 'pip install pyfiglet'

	print('\nBarBaZ Installer:'),T.sleep(2)

	print('\nUPDATE:'),a(b_1),T.sleep(2)
	print('\nAPT:'),a(b_2),T.sleep(2)
	print('\nPIP:'),a(b_3),T.sleep(2)

if __name__ == '__main__':
	clean()
	main()