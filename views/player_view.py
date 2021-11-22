import os
from pprint import pprint


class PlayersView:
	def __init__(self):
		self.view = None

	@staticmethod
	def display_menu():
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

	@staticmethod
	def prompt_for_how_many_players():
		choice = input("How many players? ")
		return choice

	@staticmethod
	def prompt_for_update_ranking():
		player_id = input("ID player? ")
		new_ranking = input("New ranking? ")
		return [player_id, new_ranking]

	@staticmethod
	def prompt_for_manual_creation_player():
		first_name = input("First name: ")
		last_name = input("Last name: ")
		ranking = input("Ranking: ")
		birth_date = input("Birth date: ")
		gender = input("Gender (F or M): ")
		description = input("Description: ")
		return [
			first_name,
			last_name,
			ranking,
			birth_date,
			gender,
			description]

	@staticmethod
	def display_players_db(db):
		players = db.table("players").all()
		for player in players:
			pprint(f"ID player = {player.doc_id}")
			pprint(player)
			print("*************")
			print("")

