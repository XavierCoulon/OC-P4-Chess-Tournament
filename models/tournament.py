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

	def save(self):
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
		controllers.main_controller.db.table("tournaments").upsert(
			serialized_tournament,
			controllers.main_controller.User.name == self.name
		)


def add_players(doc_id, players):
	tournament = unserialize(doc_id)
	tournament.players_list = players
	tournament.save()
	print(f"OK, {len(players)} players have been allocated to ID Tournament {doc_id}.")


def unserialize(doc_id):
	tournament = controllers.main_controller.db.table("tournaments").get(doc_id=int(doc_id))
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


def first_pairing(doc_id):
	table_players = controllers.main_controller.db.table("players")
	players_list = controllers.main_controller.db.table("tournaments").get(doc_id=doc_id).get("players_list")
	ranking_list = []
	players_ranking_list = []
	for player in players_list:
		ranking = table_players.get(doc_id=player).get("ranking")
		ranking_list.append(ranking)

	for player, ranking in zip(players_list, ranking_list):
		players_ranking_list.append([player, ranking])

	print(players_ranking_list)
	test = sorted(players_ranking_list, key=lambda element : element[1])
	print(test)
	for first, second in zip(test, test[int(len(test)/2):]):
		print(first[0], second[0])
	#table.update({"players_list": players}, doc_ids=[int(doc_id)])
	#print(f"OK, {len(players)} players have been allocated to ID Tournament {doc_id}.")


if __name__ == "__main__":
	tournament = controllers.main_controller.db.table("tournaments").get(doc_id=1)
	print(tournament["dates"])
	print(Tournament(dates=tournament["dates"]).dates)
