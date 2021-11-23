import controllers.main_controller
import models.tournament
import models.match


class Round:
	def __init__(self, name=None, start_date=None, end_date=None, match_list=None, finished=False):
		self.name = name
		self.start_date = start_date
		self.end_date = end_date
		self.match_list = match_list
		self.finished = finished

	def serialize(self):
		serialized_round = {
			"name": self.name,
			"start_date": self.start_date,
			"end_date": self.end_date,
			"match_list": self.match_list,
			"finished": self.finished
		}
		return serialized_round

	def first_pairing(self, tournament_name):
		table_players = controllers.main_controller.db.table("players")
		players_list = controllers.main_controller.db.table("tournaments").get(
			controllers.main_controller.User.name == tournament_name).get("players_list")
		ranking_list = []
		players_ranking = []
		matchs = []

		for player in players_list:
			ranking = table_players.get(doc_id=int(player)).get("ranking")
			ranking_list.append(ranking)
		for player, ranking in zip(players_list, ranking_list):
			players_ranking.append([player, ranking])
		sorted_players_ranking = sorted(players_ranking, key=lambda element: element[1])
		for first, second in zip(sorted_players_ranking, sorted_players_ranking[int(len(sorted_players_ranking) / 2):]):
			match = models.match.Match(player1_id=first[0], player2_id=second[0])
			matchs.append(match.serialize())
		self.match_list = matchs
		self.name = 1
		return self.serialize()


def unserialize(tournament_name, round_number):
	tournament = models.tournament.unserialize_tournament(tournament_name)
	new_round = tournament.rounds_list[round_number-1]
	return Round(
		name=new_round["name"],
		start_date=new_round["start_date"],
		end_date=new_round["end_date"],
		match_list=new_round["match_list"],
		finished=new_round["finished"])


if __name__ == "__main__":
	pass
