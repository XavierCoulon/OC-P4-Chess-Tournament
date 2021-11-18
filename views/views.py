import os
from pprint import pprint


class HomeView():
	def __init__(self):
		pass

	def display_menu(self):
		print("******* HOME MENU *******")
		print("1. PLAYERS")
		print("2. TOURNAMENT")
		print("3. QUIT")
		choice = int(input("Votre choix: "))
		os.system('cls' if os.name == "nt" else "clear")
		return choice


class PlayersView:
	def __init__(self):
		self.view = None

	def display_menu(self):
		print("******* PLAYERS MENU *******")
		print("1. create manually a player.")
		print("2. create automatically x player(s).")
		print("3. display players.")
		print("4. back to Home menu.")
		print("5. QUIT.")
		choice = int(input("Votre choix: "))
		os.system('cls' if os.name == "nt" else "clear")
		return choice

	def prompt_for_how_many_players(self):
		choice = input("How many players? ")
		return choice

	def prompt_for_manual_creation_player(self):
		first_name = input("First name: ")
		last_name = input("Last name: ")
		return [first_name, last_name]

	def display_players_db(self, db):
		pprint(db.table("players").all())

	def end(self):
		print("Fin.")


class TournamentsView:
	def __init__(self):
		self.view = None

	def display_menu(self):
		print("******* TOURNAMENT MENU *******")
		print("1. create automatically tournament.")
		print("2. display tournament.")
		print("3. back to Home menu.")
		print("4. QUIT.")
		choice = int(input("Votre choix: "))
		os.system('cls' if os.name == "nt" else "clear")
		return choice

	def display_tournaments_db(self, db):
		pprint(db.table("tournaments").all())

	def end(self):
		print("Fin.")