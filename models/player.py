""" Player class and methods """

from faker import Faker
from random import randint, choice
from datetime import datetime
from controllers.main_controller import table_players, User


class Player:
	""" Player class """
	def __init__(self, ranking=1, first_name=None, last_name=None, birth_date=None, gender=None, description=None):
		self.ranking = ranking
		self.first_name = first_name
		self.last_name = last_name
		self.birth_date = birth_date
		self.gender = gender
		self.description = description

	def __str__(self):
		""" Used to print a Player object """
		print(f"Player: {self.first_name} {self.last_name}  / ranking: {self.ranking}")

	# @property
	# def ranking(self):
	# 	return self._ranking
	#
	# @ranking.setter
	# def ranking(self, value):
	# 	while not value.isdigit():
	# 		return print("error")
	# 	self._ranking = value

	def auto_creation(self):
		""" Used to create automatically a player, using Faker module """
		fake = Faker("fr_FR")
		self.ranking = randint(1, 300)
		self.first_name = fake.first_name()
		self.last_name = fake.last_name()
		self.birth_date = datetime.strftime(fake.date_of_birth(), "%m/%d/%Y")
		self.gender = choice(["F", "M"])
		self.description = fake.text(max_nb_chars=20)

	def serialize(self):
		""" Serialize a Player object

		Returns:
		- a dictionnary
		"""
		return {
			"ranking": self.ranking,
			"first_name": self.first_name,
			"last_name": self.last_name,
			"birth_date": self.birth_date,
			"gender": self.gender,
			"description": self.description
		}

	def save(self):
		""" Save player in the database, table 'players' (creating or updating the element) """
		table_players.upsert(
			self.serialize(),
			User.first_name == self.first_name and User.
			last_name == self.last_name and User.birth_date == self.birth_date
		)

	def update_ranking(self, ranking):
		""" Update ranking of a player

		Args:
			ranking: new value of the ranking

		"""
		self.ranking = ranking

	@staticmethod
	def deserialize(player_dict):
		""" Deserialize a player from a dictionnary

		Args:
			player_dict: player

		Returns:
			Player object
		"""
		player = table_players.get(doc_id=player_dict)
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
