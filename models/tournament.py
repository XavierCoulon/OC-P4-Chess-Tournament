from faker import Faker
from random import choice
from controllers.main_controller import User, table_tournament


class Tournament:
	def __init__(
				self,
				name=None,
				location=None,
				players_list=None,
				rounds_list=None,
				dates=None,
				game_type=None,
				description=None
				):
		self.name = name
		self.location = location
		self.dates = dates
		self.players_list = players_list or {}
		self.rounds_list = rounds_list or []
		self.game_type = game_type
		self.description = description

	def auto_creation(self):
		fake = Faker("fr_FR")
		self.name = fake.first_name()
		self.location = fake.city()
		self.dates = []
		self.players_list = []
		self.rounds_list = []
		self.game_type = choice(["Rapid", "Bullet", "Blitz"])
		self.description = fake.text(max_nb_chars=20)

	def serialize(self):
		return {
			"name": self.name,
			"location": self.location,
			"dates": self.dates,
			"players_list": self.players_list,
			"rounds_list": self.rounds_list,
			"game_type": self.game_type,
			"description": self.description
		}

	def save(self):
		table_tournament.upsert(self.serialize(), User.name == self.name)

	def add_players(self, players):
		players_list = {}
		for player in players:
			players_list[str(player)] = 0
		self.players_list = players_list

	@staticmethod
	def deserialize(tournament_name):
		tournament = table_tournament.get(User.name == tournament_name)
		return Tournament(
			name=tournament["name"],
			location=tournament["location"],
			dates=tournament["dates"],
			players_list=tournament["players_list"],
			rounds_list=tournament["rounds_list"],
			game_type=tournament["game_type"],
			description=tournament["description"]
		)


if __name__ == "__main__":
	pass
