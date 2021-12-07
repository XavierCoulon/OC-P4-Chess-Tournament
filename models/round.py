""" Round class and methods """

from datetime import datetime
from controllers.main_controller import table_tournament, table_players, User
from models.tournament import Tournament
from models.match import Match


class Round:
	""" Round class"""

	def __init__(
		self,
		name=None,
		start_date=None,
		end_date=None,
		match_list=None,
	):
		self.name = name
		self.start_date = start_date
		self.end_date = end_date
		self.match_list = match_list

	def __str__(self):
		""" Used if Player object printed"""
		print(
			f"Round {self.name} created on "
			f"{self.start_date}, finished on {self.end_date}, {len(self.match_list)} matches.")

	def serialize(self):
		""" Serialize a Player object

		Returns:
			- a dictionnary
		"""
		return {
			"name": self.name,
			"start_date": self.start_date,
			"end_date": self.end_date,
			"match_list": self.match_list
		}

	def create_round(self, tournament_name):
		""" Create a round on a dedicated tournament

		Args:
			tournament_name (str): name of the tournament

		Returns:
			Round object

		"""

		ranking_list = []
		matches = []
		players_ranking = []
		# retrieve players' list from the database
		players_list = table_tournament.get(User.name == tournament_name).get("players_list")
		# retrieve rankings
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
				match = Match(player1_id=int(first[0]), player1_score=0, player2_id=int(second[0]), player2_score=0)
				match.__str__()
				matches.append(match.serialize())
			self.match_list = matches
			self.name = 1
		# Condition: if a round already exists
		else:
			# Retrieve matches already played in the tournament
			matchs_already_played = []
			rounds_list = table_tournament.get(User.name == tournament_name).get("rounds_list")
			for tour in rounds_list:
				for match in tour["match_list"]:
					matchs_already_played.append([match.get("player1_id"), match.get("player2_id")])

			players_ranking = sorted(players_ranking, key=lambda element: element[1])
			# Get a list witn player_id, ranking and score
			players_ranking_score = []
			for player in players_ranking:
				players_ranking_score.append(
					player + [players_list[player[0]]])
			players_ranking_score = sorted(players_ranking_score, key=lambda element: (-element[2], element[1]))

			# Get a list with only plays' ids
			players_ids = []
			for player in players_ranking_score:
				players_ids.append(int(player[0]))

			# Generate list of new matches
			match_list = []
			while len(players_ids) != 0:
				i = 0
				j = 1
				match = [players_ids[i], players_ids[j]]
				match_reverse = match[::-1]
				while (match in matchs_already_played or match_reverse in matchs_already_played) and j < (len(players_ids) - 1):
					j += 1
					match = [players_ids[i], players_ids[j]]
					match_reverse = match[::-1]
				if j == len(players_ids):
					match_list.append(players_ids[0])
					match_list.append(players_ids[1])
					players_ids.remove(match[0])
					players_ids.remove(match[1])
				else:
					match_list.append(match)
					players_ids.remove(match[0])
					players_ids.remove(match[1])

			new_round = []
			for match in match_list:
				match = Match(player1_id=int(match[0]), player1_score=0, player2_id=int(match[1]), player2_score=0)
				match.__str__()
				new_round.append(match.serialize())
			self.match_list = new_round
			self.name += 1

		self.start_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		self.end_date = None
		self.__str__()
		return self

	def close(self):
		""" Close a round, automatic after resulting all matches"""
		self.end_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

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
				match_list=new_round.get("match_list"))


if __name__ == "__main__":
	pass
