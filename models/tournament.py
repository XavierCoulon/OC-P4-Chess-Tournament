import controllers.main_controller


from faker import Faker
from random import choice
from controllers.main_controller import User


class Tournament:
	def __init__(
				self,
				name=None,
				location=None,
				dates=None,
				rounds_number=4,
				players_list=None,
				rounds_list=None,
				game_type=None,
				description=None
				):
		self.name = name
		self.location = location
		self.dates = dates
		self.rounds_number = rounds_number
		self.players_list = players_list
		self.rounds_list = rounds_list
		self.game_type = game_type
		self.description = description

	def auto_creation(self):
		fake = Faker("fr_FR")
		self.name = fake.first_name()
		self.location = fake.city()
		self.dates = []
		self.rounds_number = 4
		self.players_list = []
		self.rounds_list = []
		self.game_type = choice(["Rapid", "Bullet", "Blitz"])
		self.description = fake.text(max_nb_chars=20)

	def serialize(self):
		serialized_tournament = {
			"name": self.name,
			"location": self.location,
			"dates": self.dates,
			"rounds_number": self.rounds_number,
			"players_list": self.players_list,
			"rounds_list": self.rounds_list,
			"game_type": self.game_type,
			"description": self.description
		}
		return serialized_tournament

	def save(self, serialized_tournament):
		controllers.main_controller.db.table("tournaments").upsert(
			serialized_tournament,
			controllers.main_controller.User.name == self.name)


def add_players(tournament_name, players):
	tournament = unserialize_tournament(tournament_name)
	tournament.players_list = players
	tournament.save(tournament.serialize())
	print(f"OK, {len(players)} players have been allocated to Tournament {tournament_name}.")


def unserialize_tournament(tournament_name):
	tournament = controllers.main_controller.db.table("tournaments").get(User.name == tournament_name)
	return Tournament(
		name=tournament["name"],
		location=tournament["location"],
		dates=tournament["dates"],
		rounds_number=tournament["rounds_number"],
		players_list=tournament["players_list"],
		rounds_list=tournament["rounds_list"],
		game_type=tournament["game_type"],
		description=tournament["description"]
	)


if __name__ == "__main__":
	pass
