import os


class HomeView:
	def __init__(self):
		pass

	@staticmethod
	def display_menu():
		print("******* HOME MENU *******")
		print("1. PLAYERS")
		print("2. TOURNAMENT")
		print("3. REPORTS")
		print("4. QUIT")
		choice = int(input("Votre choix: "))
		os.system('cls' if os.name == "nt" else "clear")
		return choice
