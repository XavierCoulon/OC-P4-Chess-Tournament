import os
from pprint import pprint
from controllers.main_controller import table_tournament, table_players


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
		print("5. create new round.")
		print("6. result a round.")
		print("7. back to Home menu.")
		print("8. QUIT.")
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
	def display_tournaments():
		for tournoi in table_tournament:
			pprint(f"Tournament: ID={tournoi.doc_id}| {tournoi.get('name')} | {tournoi.get('game_type')}")
			pprint(f"Description: {tournoi.get('description')}")
			pprint(f"Dates: {tournoi.get('description')}")
			print("*************")

	@staticmethod
	def prompt_for_selecting_tournament():
		tournament_name = input("Tournament name: ")
		#pprint(f"Round 1 has been created for Tournament  name {tournament_name}.")
		return tournament_name

	@staticmethod
	def prompt_for_round_created():
		pass
