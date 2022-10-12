from random import randint
from time import sleep
from os import system
from colorama import init
init()

def setClear():
	system("cls")

while True:
	print(f'\033[1;32m{randint(0,9)} \033[m' *50)
	sleep(0.4)
	setClear()
