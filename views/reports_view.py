""" User's view / interface regarding reports"""

import os


class ReportsView:
	""" Class for Reports' view"""

	@staticmethod
	def display_menu():
		""" Display Reports menu"""
		print("******* REPORTS MENU *******")
		print("1. All players (sorted by ranking).")
		print("2. All players (sorted by name).")
		print("3. All players of a tournament (sorted by ranking).")
		print("4. All players of a tournament (sorted by name).")
		print("5. All players of a tournament (sorted by score).")
		print("6. All tournaments.")
		print("7. All rounds of a tournament.")
		print("8. All matches of a tournament.")
		print("9. Back to Home Menu.")
		print("10. QUIT.")
		choice = input("Your choice: ")
		os.system('cls' if os.name == "nt" else "clear")
		return choice

	@staticmethod
	def display_players(players_data):
		""" Display all players

		Args:
			players_data (list): players' datas

		"""
		print("*******PLAYER's LIST *******")
		for player in players_data:
			print(f"ID: {player[0]} | Nom: {player[1]} | Prénom: {player[2]} | Ranking: {player[3]} ")
		input("")

	@staticmethod
	def display_players_score(players_data):
		""" Display all players with score

		Args:
			players_data (list): players' datas

		"""
		print("*******PLAYER's LIST *******")
		for player in players_data:
			print(
				f"ID: {player[0]} | Nom: {player[1]} | Prénom: {player[2]} | Ranking: {player[3]} | Score: {player[4]}")
		input("")

	@staticmethod
	def display_tournaments(tournaments):
		""" Display all tournaments

		Args:
			tournaments (list): list of tournaments

		"""
		print("******* TOURNAMENT's LIST *******")
		for tournament in tournaments:
			print(
				f"Name: {tournament[0]} | ID: {tournament[1]} | Players list: {tournament[2]}"
				f" Location: {tournament[3]} | Game Type: {tournament[4]} | Description: {tournament[5]}")
		input("")

	@staticmethod
	def display_rounds(rounds_data, tournament_name):
		""" Display all rounds of a tournament

		Args:
			rounds_data (list): rounds' data
			tournament_name (str): name of a tournament

		"""
		print("*******ROUND's LIST *******")
		print(f"Tournament: {tournament_name}")
		for element in rounds_data:
			print(f"Round {element[0]} | Start date: {element[1]} | End date: {element[2]}")
		input("")

	@staticmethod
	def tournament_not_found():
		""" Message if tournament not found in database"""
		print("Tournament not found in db.")
		input("")
