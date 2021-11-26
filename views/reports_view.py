import os
from pprint import pprint
from controllers.main_controller import table_tournament, table_players


class ReportsView:
	def __init__(self):
		self.view = None

	@staticmethod
	def display_menu():
		print("******* REPORTS MENU *******")
		print("1. All players (sorted by ranking).")
		print("2. All players (sorted by name).")
		print("3. All players of a tournament (sorted by ranking).")
		print("4. All players of a tournament (sorted by name).")
		print("5. All tournaments.")
		print("6. All rounds of a tournament.")
		print("7. All matches of a tournament.")
		print("8. Back to Home Menu.")
		choice = int(input("Votre choix: "))
		os.system('cls' if os.name == "nt" else "clear")
		return choice

	@staticmethod
	def display_players(players_data):
		print("*******PLAYER's LIST *******")
		for player in players_data:
			print(f"ID: {player[0]} | Nom: {player[1]} | Prénom: {player[2]} | Ranking: {player[3]} |")
		print("")

	@staticmethod
	def display_tournaments(tournaments):
		print("******* TOURNAMENT's LIST *******")
		for tournament in tournaments:
			print(
				f"Name: {tournament[0]} | ID: {tournament[1]} | Players list: {tournament[2]}"
				f" Location: {tournament[3]} | Game Type: {tournament[4]} | Description: {tournament[5]}")
		print("")

	@staticmethod
	def display_rounds(rounds_data, tournament_name):
		print("*******ROUND's LIST *******")
		print(f"Tournament: {tournament_name}")
		for round in rounds_data:
			print(f"Round {round[0]} | Start date: {round[1]} | End date: {round[2]} | Finished: {round[3]}")
		print("")

	@staticmethod
	def display_matches(matches_data, tournament_name):
		print("*******MATCHES' LIST *******")
		print(f"Tournament: {tournament_name}")
		compteur = 1
		for round in matches_data:
			for match in round:
				print(f"Round {compteur}: Player {match[0][0]} vs {match[1][0]} (score {match[0][1]} - {match[1][1]})")
			compteur += 1
		print("")