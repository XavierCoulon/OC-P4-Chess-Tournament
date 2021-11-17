from pprint import pprint

from models.tournament import Tournament
from models.player import Player
from views.test_view import TestView
from tinydb import TinyDB, Query


class TestController:

	def __init__(self):
		self.controller = None

	def run(self):
		self.controller = True
		players = []
		new_tournament = Tournament()
		new_view = TestView()
		db = create_db()
		for player in range(new_view.prompt_for_players()):
			new_player = Player()
			player_serialized = new_player.serialize()
			new_player.save(player_serialized, db)
			players.append(new_player.last_name)
			new_tournament.players_list.append(new_player.id)

		print(new_tournament.players_list)
		pprint(db.table("players").all())


def create_db():
	db = TinyDB("db.json")
	db.table("players")
	# players_table.truncate()
	return db


if __name__ == "__main__":
	new_controller = TestController()
	new_controller.run()
