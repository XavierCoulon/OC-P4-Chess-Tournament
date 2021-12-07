""" Main controller"""

import sys
from tinydb import TinyDB, Query

# Limit of rounds by default
MAX_ROUNDS_NUMBER = 4
# Information regarding database
db = TinyDB("data/db.json", indent=4)
User = Query()
table_players = db.table("players")
table_tournament = db.table("tournaments")


class Controller:
	""" Controller class"""
	def __init__(self):
		self.controller = None
		self.view = None

	def start(self, view):
		""" To start and run a controller """
		self.controller = True
		self.view = view
		self.run()

	def run(self):
		pass


def stop():
	""" To stop the program"""
	print("Program stopped.")
	sys.exit()


if __name__ == "__main__":
	pass
