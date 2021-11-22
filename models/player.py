import controllers.main_controller

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
		self.description = fake.text(max_nb_chars=20)

	def save(self):
		serialized_player = {
			"ranking": self.ranking,
			"first_name": self.first_name,
			"last_name": self.last_name,
			"birth_date": self.birth_date,
			"gender": self.gender,
			"description": self.description
		}
		controllers.main_controller.db.table("players").upsert(
			serialized_player,
			controllers.main_controller.User.first_name == self.first_name and
			controllers.main_controller.User.last_name == self.last_name and
			controllers.main_controller.User.birth_date == self.birth_date
		)


def update(doc_id, ranking):
	player = unserialize(doc_id)
	player.ranking = ranking
	player.save()
	print(f"OK, le nouveau ranking de {doc_id} est {ranking}")


def unserialize(doc_id):
	player = controllers.main_controller.db.table("players").get(doc_id=doc_id)
	return Player(
		ranking=player["ranking"],
		first_name=player["first_name"],
		last_name=player["last_name"],
		birth_date=player["birth_date"],
		gender=player["gender"],
		description=player["description"]
)


if __name__ == "__main__":
	pass
