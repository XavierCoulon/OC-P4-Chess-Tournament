import sys

from tinydb import TinyDB, Query


MAX_ROUNDS_NUMBER = 4
db = TinyDB("data/db.json", indent=4)
User = Query()
table_players = db.table("players")
table_tournament = db.table("tournaments")


class Controller:

	def __init__(self):
		self.controller = None
		self.view = None

	def start(self, view):
		self.controller = True
		self.view = view
		self.run()

	def run(self):
		pass


def stop():
	print("FIN.")
	sys.exit()


if __name__ == "__main__":
	pass


