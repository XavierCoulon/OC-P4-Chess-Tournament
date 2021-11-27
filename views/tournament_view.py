import os
from pprint import pprint
from controllers.main_controller import table_tournament


class TournamentsView:
	def __init__(self):
		self.view = None

	@staticmethod
	def display_menu():
		print("******* TOURNAMENT MENU *******")
		print("1. Create manually a tournament.")
		print("2. Add players.")
		print("3. Create a new round.")
		print("4. Result last round.")
		print("5. Back to Home menu.")
		print("6. QUIT.")
		print("***************")
		print("7. Create automatically a tournament.")
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
		id_tournament = input("Tournament name: ")
		players = input("ID players to allocate (X Y Z..., will erase previous list): ")
		return [id_tournament, players.split()]

	@staticmethod
	def allocated_players():
		print("OK, players have been allocated.")
		input("")

	@staticmethod
	def display_tournaments():
		for tournoi in table_tournament:
			pprint(f"Tournament: ID={tournoi.doc_id}| {tournoi.get('name')} | {tournoi.get('game_type')}")
			pprint(f"Description: {tournoi.get('description')}")
			pprint(f"Dates: {tournoi.get('description')}")
			print("*************")

	@staticmethod
	def prompt_for_selecting_tournament():
		tournament_name = input("Tournament name: ")
		return tournament_name

	@staticmethod
	def players_missing():
		print("No players allocated on this tournament.")
		input("")

	@staticmethod
	def rounds_limit_reached():
		print("Limit of rounds by tournament already reached.")
		input("")
