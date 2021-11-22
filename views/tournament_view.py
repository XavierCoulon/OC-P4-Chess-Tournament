import os
from pprint import pprint


class TournamentsView:
	def __init__(self):
		self.view = None

	@staticmethod
	def display_menu():
		print("******* TOURNAMENT MENU *******")
		print("1. create manually a tournament.")
		print("2. create automatically a tournament.")
		print("3. display tournaments.")
		print("4. add players.")
		print("5. back to Home menu.")
		print("6. QUIT.")
		choice = int(input("Votre choix: "))
		os.system('cls' if os.name == "nt" else "clear")
		return choice

	@staticmethod
	def prompt_for_manual_creation_tournament():
		name = input("Name: ")
		location = input("Location: ")
		dates = input("Dates: ")
		game_type = input("Game type: ")
		description = input("Description: ")
		return [
			name,
			location,
			dates,
			game_type,
			description]

	@staticmethod
	def prompt_for_allocating_players():
		id_tournament = input("ID tournament: ")
		players = input("ID players to allocate (X Y Z..., will erase previous list): ")
		return [id_tournament, players.split()]

	@staticmethod
	def display_tournaments_db(db):
		tournois = db.table("tournaments")
		for tournoi in tournois:
			# display more info, as players_list (in progress...)
			pprint(f"ID tournament = {tournoi.doc_id}")
			pprint(tournoi)
			print("*************")
			print("")
