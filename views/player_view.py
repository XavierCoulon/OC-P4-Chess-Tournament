""" User's view / interface regarding players"""

import os


class PlayersView:
	""" View for managing players"""

	@staticmethod
	def display_menu():
		""" UI for handling players"""
		print("******* 1. PLAYERS MENU *******")
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
	def prompt_for_player_id():
		""" UI to search a player_id"""
		player_id = input("Player ID ? ")
		return player_id

	@staticmethod
	def prompt_for_first_name():
		""" Fill the first name

		Returns (str): first name

		"""
		first_name = input("First name: ")
		return first_name

	@staticmethod
	def prompt_for_last_name():
		""" Fill the last name

		Returns (str): last name

		"""
		last_name = input("Last name: ")
		return last_name

	@staticmethod
	def prompt_for_ranking():
		""" Fill the ranking

		Returns (str): ranking

		"""
		ranking = input("Ranking: ")
		return ranking

	@staticmethod
	def prompt_for_birth_date():
		""" Fill the birth date

		Returns (str): birth date

		"""
		birth_date = input("Birth date (dd/mm/yy): ")
		return birth_date

	@staticmethod
	def prompt_for_gender():
		""" Fill the gender

		Returns (str): gender

		"""
		gender = input("Gender (F or M): ")
		return gender

	@staticmethod
	def prompt_for_description():
		""" Fill the description

		Returns (str): description

		"""
		description = input("Description: ")
		print("")
		return description

	@staticmethod
	def player_not_found():
		""" Message if data not found in db"""
		print("Player ID not found in db.")
		input("")

	@staticmethod
	def invalid_format():
		""" Message if invalid format"""
		return input(" -Warning: format not valid, please retry: ")
