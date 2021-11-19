from faker import Faker
from random import randint, choice
from datetime import datetime


class Player:

	def __init__(self, ranking=None, first_name=None, last_name=None, birth_date=None, gender=None, description=None):
		self.ranking = ranking
		self.first_name = first_name
		self.last_name = last_name
		self.birth_date = birth_date
		self.gender = gender
		self.description = description

	def auto_creation(self):
		fake = Faker("fr_FR")
		self.ranking = randint(1, 20)
		self.first_name = fake.first_name()
		self.last_name = fake.last_name()
		self.birth_date = datetime.strftime(fake.date_of_birth(), "%m/%d/%Y")
		self.gender = choice(["F", "M"])
		self.description = fake.text()

	def serialize(self):
		serialized_player = {
			"ranking": self.ranking,
			"first_name": self.first_name,
			"last_name": self.last_name,
			"birth_date": self.birth_date,
			"gender": self.gender,
			"description": self.description
		}
		return serialized_player

	def unserialize(self, dicoPlayer):
		pass
		#return Player(
		#	dicoPlayer.get("name"))

	def save(self, serialized_player, db):
		db.table("players").insert(serialized_player)


if __name__ == "__main__":
	pass
