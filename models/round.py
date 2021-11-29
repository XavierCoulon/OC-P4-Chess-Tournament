from controllers.main_controller import table_tournament, table_players, User
from models.tournament import Tournament
from models.match import Match
from datetime import datetime


class Round:
	def __init__(self, name=None, start_date=None, end_date=None, match_list=None, finished=False):
		self.name = name
		self.start_date = start_date
		self.end_date = end_date
		self.match_list = match_list
		self.finished = finished

	def __repr__(self):
		print(f"Round {self.name} created on {self.start_date}. {len(self.match_list)} matches.")

	def serialize(self):
		return {
			"name": self.name,
			"start_date": self.start_date,
			"end_date": self.end_date,
			"match_list": self.match_list,
			"finished": self.finished
		}

	def create_round(self, tournament_name):
		players_list = table_tournament.get(User.name == tournament_name).get("players_list")
		ranking_list = []
		matches = []
		players_ranking = []
		for player in players_list:
			ranking = table_players.get(doc_id=int(player)).get("ranking")
			ranking_list.append(ranking)
		for player, ranking in zip(players_list, ranking_list):
			players_ranking.append([player, ranking])

		if not self.match_list:
			sorted_players_ranking = sorted(players_ranking, key=lambda element: element[1])
			for first, second in zip(sorted_players_ranking, sorted_players_ranking[int(len(sorted_players_ranking) / 2):]):
				match = Match(first[0], 0, second[0], 0)
				matches.append(match.serialize())
			self.match_list = matches
			self.name = 1
		else:
			#A REVOIR
			players_ranking = sorted(players_ranking, key=lambda element: element[0])
			players_ranking_score = []
			for player in players_ranking:
				players_ranking_score.append(player + [players_list[player[0]]])
			players_ranking_score = sorted(players_ranking_score, key=lambda element: (element[2], element[1]))
			new_round = []
			for x, y in zip(*[iter(players_ranking_score)] * 2):
				match = Match(x[0], 0, y[0], 0)
				new_round.append(match.serialize())
			self.match_list = new_round
			self.name += 1
		self.start_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		self.end_date = None
		self.finished = False
		self.__repr__()
		return self

	def close(self):
		self.finished = True
		self.end_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
		return self

	@staticmethod
	def deserialize(tournament_name):
		tournament = Tournament.deserialize(tournament_name)
		if not tournament.rounds_list:
			return Round()
		else:
			new_round = tournament.rounds_list[-1]
			return Round(
				name=new_round["name"],
				start_date=new_round["start_date"],
				end_date=new_round["end_date"],
				match_list=new_round["match_list"],
				finished=new_round["finished"])


if __name__ == "__main__":
	pass
