""" Round class and methods """

from controllers.main_controller import table_tournament, table_players, User
from models.tournament import Tournament
from models.match import Match
from datetime import datetime


class Round:
	""" Round class"""

	def __init__(
		self,
		name=None,
		start_date=None,
		end_date=None,
		match_list=None,
		finished=False
	):
		self.name = name
		self.start_date = start_date
		self.end_date = end_date
		self.match_list = match_list
		self.finished = finished

	def __str__(self):
		""" Used if Player object printed"""
		print(
			f"Round {self.name} created on "
			f"{self.start_date}. {len(self.match_list)} matches.")

	def serialize(self):
		""" Serialize a Player object

		Returns:
			- a dictionnary
		"""
		return {
			"name": self.name,
			"start_date": self.start_date,
			"end_date": self.end_date,
			"match_list": self.match_list,
			"finished": self.finished
		}

	def create_round(self, tournament_name):
		""" Create a round on a dedicated tournament

		Args:
			tournament_name (str): name of the tournament

		Returns:
			Round object

		"""

		# get back players' list
		players_list = table_tournament.get(User.name == tournament_name).get(
			"players_list")
		ranking_list = []
		matches = []
		players_ranking = []
		# get back rankings
		for player in players_list:
			ranking = table_players.get(doc_id=int(player)).get("ranking")
			ranking_list.append(ranking)
		for player, ranking in zip(players_list, ranking_list):
			players_ranking.append([player, ranking])

		# Condition: no round existing in the tournament
		if not self.match_list:
			sorted_players_ranking = sorted(players_ranking, key=lambda element: element[1])
			for first, second in zip(
				sorted_players_ranking,
				sorted_players_ranking[int(len(sorted_players_ranking) / 2):]
			):
				match = Match(first[0], 0, second[0], 0)
				match.__str__()
				matches.append(match.serialize())
			self.match_list = matches
			self.name = 1
		# Condition: if a round already exists
		else:
			# To be reviewed
			players_ranking = \
				sorted(players_ranking, key=lambda element: element[0])
			players_ranking_score = []
			for player in players_ranking:
				players_ranking_score.append(
					player + [players_list[player[0]]])
			players_ranking_score = \
				sorted(players_ranking_score, key=lambda element: (element[2], element[1]))
			new_round = []
			for x, y in zip(*[iter(players_ranking_score)] * 2):
				match = Match(x[0], 0, y[0], 0)
				match.__str__()
				new_round.append(match.serialize())
			self.match_list = new_round
			self.name += 1
		self.start_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		self.end_date = None
		self.finished = False
		self.__str__()
		return self

	def close(self):
		""" Close a round, automatic after resulting all matches"""
		self.finished = True
		self.end_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

	# return self

	@staticmethod
	def deserialize(tournament_name):
		""" Deserialize the last round of a tournament (from a dictionnary)

		Args:
			tournament_name: name of a tournament

		Returns:
			Round object
		"""
		tournament = Tournament.deserialize(tournament_name)
		if not tournament.rounds_list:
			return Round()
		else:
			# get last round
			new_round = tournament.rounds_list[-1]
			return Round(
				name=new_round.get("name"),
				start_date=new_round.get("start_date"),
				end_date=new_round.get("end_date"),
				match_list=new_round.get("match_list"),
				finished=new_round.get("finished"))


if __name__ == "__main__":
	pass
