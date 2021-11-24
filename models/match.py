class Match:
	def __init__(self, player1_id=None, player2_id=None, player1_result=None, player2_result=None):
		self.player1_id = player1_id
		self.player2_id = player2_id
		self.player1_result = player1_result
		self.player2_result = player2_result

	def serialize(self):
		return {
			"player1_id": self.player1_id,
			"player2_id": self.player2_id,
			"player1_result": self.player1_result,
			"player2_result": self.player2_result,
		}

	def result(self, player1_result, player2_result):
		self.player1_result = player1_result
		self.player2_result = player2_result
		return self


def deserialize(match):
	return Match(
		player1_id=match["player1_id"],
		player2_id=match["player2_id"],
		player1_result=match["player1_result"],
		player2_result=match["player2_result"],
	)

