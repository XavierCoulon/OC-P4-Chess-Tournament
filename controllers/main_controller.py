import sys

from tinydb import TinyDB

db = TinyDB("data/db.json", indent=4)
db.table("players")
db.table("tournaments")


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


def update(doc_id, ranking):
	table = db.table("players")
	table.update({"ranking": ranking}, doc_ids=[doc_id])
	print(f"OK, le nouveau ranking de {doc_id} est {ranking}")


def stop():
	print("FIN.")
	sys.exit()


if __name__ == "__main__":
	pass


