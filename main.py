from colorama import init
from colorama import Fore, Back, Style
import os
init()


class Purse:
	def __init__(self):
		self.__money = 0.00

	def info(self):
		return self.__money

	def top_up_balance(self, amount):
		print('Successfully')
		self.__money = self.__money + amount

	def top_down_balance(self, amount):
		if self.__money - amount < 0:
			print('Error: Insufficient money')
		else: 
			print('Successfully!')
			self.__money = self.__money - amount



def PurseHome(name):
	y = os.get_terminal_size().columns
	space = ' '
	print(Back.GREEN + space*int((y/2)) + f'hello {name}' + space*int((y/2)))




def main():
	while True:
		login = input('Login: ')
		password = input('Password: ')
		if login == 'admin' and password == 'admin':
			PurseHome(login)
			purse = Purse()
			while True: 
				Style.RESET_ALL
				print(Fore.RED + '1. Show curent balance')
				print(Fore.RED + '2. Top up')
				print(Fore.RED + '3. Transfer money')
				choise = int(input('Your choise: '))
				
				if choise == 1:
					print(purse.info())

				elif choise == 2:
					amount = int(input('Enter the amount: '))
					purse.top_up_balance(amount)
					print(f'Your current balance: {purse.info()}')

				elif choise == 3:
					amount = int(input('Enter the amount: '))
					purse.top_down_balance(amount)
					print(f'Your current balance: {purse.info()}')

				else:
					print('incorrect, try again')
		else:
			print('incorrect login or password, please try again')
if __name__ == "__main__":
	main()