from faker import Faker
from random import choice


class Tournament:
	def __init__(self):
		fake = Faker("fr_FR")
		self.name = fake.first_name()
		self.location = fake.city()
		self.dates = []
		self.rounds_number = 4
		self.players_list = []
		self.rounds_list = []
		self.game_type = choice(["Rapid", "Bullet", "Blitz"])
		self.description = fake.text()


if __name__ == "__main__":
	new_tournament = Tournament()
	print(new_tournament.name)
	print(new_tournament.location)
	print(new_tournament.rounds_number)
	print(new_tournament.game_type)
	print(new_tournament.description)