class Match:
	def __init__(self, tournament, player1_id, player2_id, player1_result=None, player2_result=None):
		self.player1_id = player1_id
		self.player2_id = player2_id
		self.player1_result = player1_result
		self.player2_result = player2_result
		self.tournament = tournament # utile ?

	def result(self, player1_result, player2_result):
		self.player1_result = player1_result
		self.player2_result = player2_result
		return  # utile ?



