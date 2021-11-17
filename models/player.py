from faker import Faker
from random import randint, choice
from tinydb import TinyDB


class Player:
	id_counter = 1

	def __init__(self):
		fake = Faker("fr_FR")
		self.id = Player.id_counter
		Player.id_counter += 1
		self.first_name = fake.first_name()
		self.last_name = fake.last_name()
		self.birth_date = fake.date_of_birth()
		self.gender = choice(["F", "M"])
		self.description = fake.text()
		self.ranking = randint(1, 100)

	def serialize(self):
		serialized_player = {
			"last_name": self.last_name,
			"first_name": self.first_name,
			"id": self.id,
			"ranking": self.ranking
		}
		return serialized_player

	def save(self, serialized_player, db):
		db.table("players").insert(serialized_player)


if __name__ == "__main__":
	for _ in range(8):
		new_player = Player()
		print(new_player.first_name)
		print(new_player.id)
