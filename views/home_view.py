""" View of Home menu"""

import os


class HomeView:
	""" View for home menu"""

	@staticmethod
	def display_menu():
		""" Display Home menu"""
		print("******* HOME MENU *******")
		print("1. PLAYERS")
		print("2. TOURNAMENTS")
		print("3. REPORTS")
		print("4. QUIT")
		choice = input("Your choice: ")
		os.system('cls' if os.name == "nt" else "clear")
		return choice
