from faker import Faker
from random import choice


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
		self.description = fake.text()

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

	def save(self, serialized_tournament, db):
		db.table("tournaments").insert(serialized_tournament)


if __name__ == "__main__":
	pass