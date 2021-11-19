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

	@staticmethod
	def display_menu(self):
		print("******* PLAYERS MENU *******")
		print("1. create manually a player.")
		print("2. create automatically x player(s).")
		print("3. display players.")
		print("4. change ranking player.")
		print("5. back to Home menu.")
		print("6. QUIT.")
		choice = int(input("Votre choix: "))
		os.system('cls' if os.name == "nt" else "clear")
		return choice

	def prompt_for_how_many_players(self):
		choice = input("How many players? ")
		return choice

	def prompt_for_update_ranking(self):
		player_id = input("ID player? ")
		new_ranking = input("New ranking? ")
		return [player_id, new_ranking]

	def prompt_for_manual_creation_player(self):
		first_name = input("First name: ")
		last_name = input("Last name: ")
		return [first_name, last_name]

	def display_players_db(self, db):
		players = db.table("players").all()
		for player in players:
			pprint(f"ID player = {player.doc_id}")
			pprint(player)
			print("*************")
			print("")


class TournamentsView:
	def __init__(self):
		self.view = None

	def display_menu(self):
		print("******* TOURNAMENT MENU *******")
		print("1. create automatically tournament.")
		print("2. display tournaments.")
		print("3. back to Home menu.")
		print("4. QUIT.")
		choice = int(input("Votre choix: "))
		os.system('cls' if os.name == "nt" else "clear")
		return choice

	def display_tournaments_db(self, db):
		pprint(db.table("tournaments").all())
