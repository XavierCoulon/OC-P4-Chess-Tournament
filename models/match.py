""" Match class and methods """

from controllers.main_controller import table_players


class Match:
	"""Match class"""
	def __init__(self, player1_id=None, player1_score=None, player2_id=None, player2_score=None, player1_name=None, player2_name=None):
		self.player1_id = player1_id
		self.player2_id = player2_id
		self.player1_score = player1_score
		self.player2_score = player2_score
		self.player1_name = table_players.get(doc_id=self.player1_id).get("last_name")
		self.player2_name = table_players.get(doc_id=self.player2_id).get("last_name")

	def __str__(self):
		""" Used to print a Round object """
		print(f"Player {self.player1_id} - {self.player1_name} vs Player {self.player2_id} - {self.player2_name} (score: {self.player1_score} - {self.player2_score})")

	def serialize(self):
		""" Serialize a Player object

		Returns:
		- a dictionnary
		"""
		return {
			"player1_id": self.player1_id,
			"player1_score": self.player1_score,
			"player2_id": self.player2_id,
			"player2_score": self.player2_score,
			"player1_name": self.player1_name,
			"player2_name": self.player2_name
		}

	def result(self, result, tournament):
		""" Result a match

		Args:
			result: result of the match (1N2)
			tournament: name of the tournament

		"""
		if result == "1":
			self.player1_score = 1
			tournament.players_list[str(self.player1_id)] += 1
			self.player2_score = 0
		elif result == "N":
			self.player1_score = 0.5
			self.player2_score = 0.5
			tournament.players_list[str(self.player1_id)] += 0.5
			tournament.players_list[str(self.player2_id)] += 0.5
		else:
			self.player2_score = 1
			tournament.players_list[str(self.player2_id)] += 1
			self.player1_score = 0

	@staticmethod
	def deserialize(match):
		""" Deserialize a match (from a dictionnary)

		Args:
			match (dict): match

		Returns:
			Match object
		"""
		return Match(
			player1_id=match.get("player1_id"),
			player1_score=match.get("player1_score"),
			player2_id=match.get("player2_id"),
			player2_score=match.get("player2_score"),
			player1_name=match.get("player1_name"),
			player2_name=match.get("player2_name")
		)


if __name__ == "__main__":
	match = Match(player1_id="1", player2_id="2")
	print(match.player1_name)
	print(match.player2_name)