""" Tournament class and methods """

from faker import Faker  # to generate automatically a fake tournament
from random import choice
from controllers.main_controller import User, table_tournament


class Tournament:
	""" Tournament class"""
	def __init__(
		self,
		name=None,
		location=None,
		players_list=None,
		rounds_list=None,
		dates=None,
		game_type=None,
		description=None):
		self.name = name
		self.location = location
		self.dates = dates
		# players_list :  {"player_id": score in the tournament}
		self.players_list = players_list or {}
		self.rounds_list = rounds_list or []
		self.game_type = game_type
		self.description = description

	def __str__(self):
		""" Used to print a Tournament object """
		print(f"Tournament '{self.name}  / Player: {self.players_list} / Game type: {self.game_type}' created.")

	def auto_creation(self):
		""" Used to create automatically a tournament, using Faker module """
		fake = Faker("fr_FR")
		self.name = fake.first_name()
		self.location = fake.city()
		self.dates = []
		self.players_list = {}
		self.rounds_list = []
		self.game_type = choice(["Rapid", "Bullet", "Blitz"])
		self.description = fake.text(max_nb_chars=20)

	def save(self):
		""" Save tournament in the database, table players (creating or updating the element) """
		table_tournament.upsert(self.serialize(), User.name == self.name)

	def add_players(self, players):
		""" Allocate players to a tournament (dictionnary {"player_id": score in the tournament}, score = 0)

		Args:
			players: list of ID players (string format: 'X Y Z')

		"""
		players_list = {}
		for player in players:
			players_list[str(player)] = 0
		self.players_list = players_list

	def update_global_score (self, result):
		""" Update global score for each player in players_list (following resut of a match)

		Args:
			result (list): player1_id, player1_score, player2_id, player2_score

		"""
		self.players_list[str(result[0])] += result[1]
		self.players_list[str(result[2])] += result[3]

	def serialize(self):
		""" Serialize a Player object

			Returns:
			- a dictionnary
		"""
		return {
			"name": self.name,
			"location": self.location,
			"dates": self.dates,
			"players_list": self.players_list,
			"rounds_list": self.rounds_list,
			"game_type": self.game_type,
			"description": self.description
		}

	@staticmethod
	def deserialize(tournament_name):
		""" Deserialize a tournament from a dictionnary

		Args:
			tournament_name: tournament

		Returns:
			Player object
		"""
		tournament = table_tournament.get(User.name == tournament_name)
		return Tournament(
			name=tournament.get("name"),
			location=tournament.get("location"),
			dates=tournament.get("dates"),
			players_list=tournament.get("players_list"),
			rounds_list=tournament.get("rounds_list"),
			game_type=tournament.get("game_type"),
			description=tournament.get("description")
		)


if __name__ == "__main__":
	pass
