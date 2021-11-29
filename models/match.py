class Match:
	def __init__(self, player1_id=None, player1_score=None, player2_id=None, player2_score=None):
		self.player1_id = player1_id
		self.player2_id = player2_id
		self.player1_score = player1_score
		self.player2_score = player2_score

	def __repr__(self):
		print(f"Player {self.player1_id} vs player {self.player2_id} (score: {self.player1_score} - {self.player2_score})")

	def serialize(self):
		return {
			"player1_id": self.player1_id,
			"player1_score": self.player1_score,
			"player2_id": self.player2_id,
			"player2_score": self.player2_score
		}

	def result(self, result, tournament):
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
		return self

	@staticmethod
	def deserialize(match):
		return Match(
			player1_id=match["player1_id"],
			player1_score=match["player1_score"],
			player2_id=match["player2_id"],
			player2_score=match["player2_score"]
		)
