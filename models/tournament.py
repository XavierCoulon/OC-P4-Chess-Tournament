import controllers.main_controller

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

	@staticmethod
	def save(serialized_tournament):
		controllers.main_controller.db.table("tournaments").insert(serialized_tournament)


def add_players(doc_id, players):
	table = controllers.main_controller.db.table("tournaments")
	table.update({"players_list": players}, doc_ids=[int(doc_id)])
	print(f"OK, {len(players)} players have been allocated to ID Tournament {doc_id}.")


if __name__ == "__main__":
	pass
