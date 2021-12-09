""" Main controller"""

import sys
import os
from tinydb import TinyDB, Query


# Information regarding database
data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
if not os.path.exists(data_folder):
	os.mkdir(data_folder)
db = TinyDB(os.path.join(data_folder, "db.json"), indent=4)
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

	@staticmethod
	def stop():
		""" To stop the program"""
		print("Program stopped.")
		sys.exit()


if __name__ == "__main__":
	pass
