import sys

from tinydb import TinyDB, Query

db = TinyDB("data/db.json", indent=4)
User = Query()
db.table("players")
db.table("tournaments")
db.table("rounds")


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


