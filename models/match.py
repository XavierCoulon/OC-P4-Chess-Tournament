class Match:
	def __init__(self, tournament, player1_id, player2_id, player1_result=None, player2_result=None):
		self.player1_id = player1_id
		self.player2_id = player2_id
		self.player1_result = player1_result
		self.player2_result = player2_result
		self.tournament = tournament # utile ?

	def unserialize(tournament_id, round_number, ):
		tournament = models.tournament.unserialize(tournament_id)
		round = tournament.rounds_list[round_number - 1]
		return Round(
			name=round["name"],
			start_date=round["start_date"],
			end_date=round["end_date"],
			match_list=tournament["match_list"],
		)


	def result(self, player1_result, player2_result):
		self.player1_result = player1_result
		self.player2_result = player2_result
		return  # utile ?



