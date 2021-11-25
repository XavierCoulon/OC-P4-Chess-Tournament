import models.tournament
from models.match import Match
from controllers.main_controller import table_tournament, table_players, User


class Round:
	def __init__(self, name=None, start_date=None, end_date=None, match_list=None, finished=False):
		self.name = name
		self.start_date = start_date
		self.end_date = end_date
		self.match_list = match_list
		self.finished = finished

	def serialize(self):
		return {
			"name": self.name,
			"start_date": self.start_date,
			"end_date": self.end_date,
			"match_list": self.match_list,
			"finished": self.finished
		}

	def first_pairing(self, tournament_name):
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
				match = [[first[0], 0], [second[0], 0]]
				matches.append(match)
			self.match_list = matches
			self.name = 1
		else:
			players_ranking = sorted(players_ranking, key=lambda element: element[0])
			last_round = self.match_list
			refactor_last_round = []
			for item in last_round:
				refactor_last_round.append(item[0])
				refactor_last_round.append(item[1])
			print(refactor_last_round)
			refactor_last_round = sorted(refactor_last_round, key=lambda element: element[0])
			last_round_ranking = [
				[x[0], x[1], y[1]] if x[0] == y[0] else 0 for (x, y) in zip(refactor_last_round, players_ranking)]
			last_round_ranking = sorted(last_round_ranking, key=lambda x: (x[1], -x[2], x[0]), reverse=True)
			new_round = []
			for x, y in zip(*[iter(last_round_ranking)] * 2):
				new_round.append([x, y])
			self.match_list = new_round
			self.name += 1
			self.finished = False
		return self

	def result_match(self):
		for match in self.match_list:
			choice = input(f"Result match 'player {match[0][0]} vs player {match[1][0]}' (1/N/2): ")
			if choice == "1":
				match[0][1] += 1
				match[1][1] += 0
			elif choice == "N":
				match[0][1] += 0.5
				match[1][1] += 0.5
			else:
				match[0][1] += 0
				match[1][1] += 1
		self.finished = True
		return self


def deserialize_round(tournament_name):
	tournament = models.tournament.deserialize_tournament(tournament_name)
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
