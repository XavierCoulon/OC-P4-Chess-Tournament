import sys

from models.tournament import Tournament
from models.player import Player
from views.views import HomeView, PlayersView, TournamentsView
from tinydb import TinyDB


class HomeController:

	def __init__(self):
		self.controller = None
		self.view = HomeView()

	def start(self):
		self.controller = True
		while self.controller:
			self.run()

	def run(self):
		choice = self.view.display_menu()
		if choice == 1:
			self.controller = PlayersController()
			self.controller.start()
		elif choice == 2:
			self.controller = TournamentsController()
			self.controller.start()
		else:
			self.stop()

	def stop(self):
		sys.exit()


class PlayersController:

	def __init__(self):
		self.controller = None
		self.view = PlayersView()

	def start(self):
		self.controller = True
		while self.controller:
			self.run()

	def run(self):
		db = create_db()
		choice = self.view.display_menu()
		if choice == 1:
			player = self.view.prompt_for_manual_creation_player()
			new_player = Player(first_name=player[0], last_name=player[1])
			new_player.save(new_player.serialize(), db)
		elif choice == 2:
			number = self.view.prompt_for_how_many_players()
			for player in range(int(number)):
				new_player = Player()
				new_player.auto_creation()
				player_serialized = new_player.serialize()
				new_player.save(player_serialized, db)
		elif choice == 3:
			self.view.display_players_db(db)
		elif choice == 4:
			self.controller = HomeController()
			self.controller.start()
		else:
			self.stop()

	def stop(self):
		self.controller = None
		self.view.end()
		sys.exit()


class TournamentsController:

	def __init__(self):
		self.controller = None
		self.view = TournamentsView()

	def start(self):
		self.controller = True
		while self.controller:
			self.run()

	def run(self):
		db = create_db()
		choice = self.view.display_menu()
		if choice == 1:
			new_tournament = Tournament()
			new_tournament.auto_creation()
			new_tournament.save(new_tournament.serialize(), db)
		elif choice == 2:
			self.view.display_tournaments_db(db)
		elif choice == 3:
			self.controller = HomeController()
			self.controller.start()
		else:
			self.stop()

	def stop(self):
		self.controller = None
		self.view.end()
		sys.exit()


def create_db():
	db = TinyDB("data/db.json", indent=4)
	db.table("players")
	db.table("tournaments")
	# players_table.truncate()
	return db


if __name__ == "__main__":
	pass
