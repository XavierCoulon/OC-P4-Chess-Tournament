""" Match class and methods """


class Match:
	"""Match class"""
	def __init__(self, player1_id=None, player1_score=None, player2_id=None, player2_score=None):
		self.player1_id = player1_id
		self.player2_id = player2_id
		self.player1_score = player1_score
		self.player2_score = player2_score

	def __str__(self):
		""" Used to print a Round object """
		print(f"Player {self.player1_id} vs player {self.player2_id} (score: {self.player1_score} - {self.player2_score})")

	def serialize(self):
		""" Serialize a Player object

		Returns:
		- a dictionnary
		"""
		return {
			"player1_id": self.player1_id,
			"player1_score": self.player1_score,
			"player2_id": self.player2_id,
			"player2_score": self.player2_score
		}

	def result(self, result, tournament):
		""" Result a match

		Args:
			result: result of the match (1N2)
			tournament: name of the tournament

		"""
		if result == "1":
			self.player1_score = 1
			tournament.players_list[self.player1_id] += 1
			self.player2_score = 0
		elif result == "N":
			self.player1_score = 0.5
			self.player2_score = 0.5
			tournament.players_list[self.player1_id] += 0.5
			tournament.players_list[self.player2_id] += 0.5
		else:
			self.player2_score = 1
			tournament.players_list[self.player2_id] += 1
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
			player2_score=match.get("player2_score")
		)
