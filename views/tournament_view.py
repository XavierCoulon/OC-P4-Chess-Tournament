""" User's view / interface regarding tournament"""

import os


class TournamentsView:
	""" View for managing tournament"""

	@staticmethod
	def display_menu():
		""" UI for handling players"""
		print("******* TOURNAMENT MENU *******")
		print("1. Create manually a tournament.")
		print("2. Add players.")
		print("3. Create a new round.")
		print("4. Result last round.")
		print("5. Back to Home menu.")
		print("6. QUIT.")
		choice = input("Your choice: ")
		os.system('cls' if os.name == "nt" else "clear")
		return choice

	@staticmethod
	def prompt_for_manual_creation_tournament():
		""" UI to create manually a tournament
		Returns: list of all values filled

		"""""
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
	def prompt_for_name():
		""" Fill the name

		Returns (str): name

		"""
		name = input("Name: ")
		return name

	@staticmethod
	def prompt_for_date():
		""" Fill the date

		Returns (str): date

		"""
		date = input("Date (dd/mm/yy): ")
		return date

	@staticmethod
	def prompt_for_location():
		""" Fill the location

		Returns (str): location

		"""
		location = input("Location: ")
		return location

	@staticmethod
	def prompt_for_game_type():
		""" Fill the game type

		Returns (str): game type

		"""
		game_type = input("Game type (Rapid, Bullet or Blitz) : ")
		return game_type

	@staticmethod
	def prompt_for_description():
		""" Fill the description

		Returns (str): description

		"""
		description = input("Description: ")
		return description


	@staticmethod
	def prompt_for_allocating_players():
		""" UI to allocate players to a a tournament

		Returns: list with the name of the tournament and list of players

		"""""
		tournament_name = input("Tournament name: ")
		players = input("ID players to allocate (X Y Z..., will erase previous list): ")
		return [tournament_name, players.split()]

	@staticmethod
	def allocated_players():
		"""Message when players have been allocated."""
		print("OK, players have been allocated.")
		input("")

	@staticmethod
	def prompt_for_selecting_tournament():
		""" UI to select a tournament

		Returns: name of the tournament (string)

		"""
		tournament_name = input("Tournament name: ")
		return tournament_name

	@staticmethod
	def tournament_not_found():
		""" Message if tournament not found in database"""
		print("Tournament not found in db.")
		input("")

	@staticmethod
	def player_not_found(player):
		""" Message if player not found in database"""
		print(f"Player ID {player} not found in db.")
		input("")

	@staticmethod
	def uneven_players():
		""" Message if number of players is uneven """
		print("Numbers of players uneven.")
		input("")

	@staticmethod
	def prompt_for_resulting(player1_id, player2_id, player1_name, player2_name):
		""" UI for resulting matches of last round

		Args:
			player1_id (str): ID player 1
			player2_id (str): ID player 2
			player1_name (str): player 1 last name
			player2_name (str): player 2 last name

		Returns:
			result (str): result of input
		"""
		result = input(f"Result match Player {player1_id} - {player1_name} vs Player {player2_id} - {player2_name}' (1/N/2): ")
		return result

	@staticmethod
	def players_missing():
		""" Message if no players have been allocated on the tournament (checked in database)."""
		print("No players allocated on this tournament.")
		input("")

	@staticmethod
	def rounds_limit_reached():
		""" Message if limit of rounds by tournament has been reached (cf. constant MAX_ROUNDS_NUMBER in Maincontroller)"""
		print("Limit of rounds by tournament already reached.")
		input("")

	@staticmethod
	def invalid_format():
		""" Message if invalid format"""
		return input(" -Warning: format not valid, please retry: ")