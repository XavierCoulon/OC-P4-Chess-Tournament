""" User's view / interface regarding players"""

import os


class PlayersView:
	""" View for managing players"""
	def __init__(self):
		self.view = None

	@staticmethod
	def display_menu():
		""" UI for handling players"""
		print("******* PLAYERS MENU *******")
		print("1. Create manually a player.")
		print("2. Change player's ranking.")
		print("3. Back to Home menu.")
		print("4. QUIT.")
		choice = input("Your choice: ")
		os.system('cls' if os.name == "nt" else "clear")
		return choice

	@staticmethod
	def prompt_for_how_many_players():
		""" UI for player automatic creation"""
		choice = input("How many players? ")
		return choice

	@staticmethod
	def prompt_for_update_ranking():
		""" UI for updating ranking's player"""
		player_id = input("ID player? ")
		new_ranking = int(input("New ranking? "))
		return [player_id, new_ranking]

	@staticmethod
	def prompt_for_manual_creation_player():
		""" UI to create a player

		Returns: list of values filled

		"""

		first_name = input("First name: ")
		last_name = input("Last name: ")
		ranking = int(input("Ranking: "))
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
	def player_not_found():
		""" Message if data not found in db"""
		print("Player not found in db.")
		input("")

	# Not used so far
	# @staticmethod
	# def display_format_invalid():
	# 	value = input("Format invalid, please retry: ")
	# 	return value
