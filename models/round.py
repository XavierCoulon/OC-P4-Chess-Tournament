import controllers.main_controller
import models.tournament


class Round:
	def __init__(self, name=None, start_date=None, end_date=None, match_list=None, finished=False):
		self.name = name
		self.start_date = start_date
		self.end_date = end_date
		self.match_list = match_list
		self.finished = finished

	def serialize(self):
		serialized_round= {
			"name": self.name,
			"start_date": self.start_date,
			"end_date": self.end_date,
			"match_list": self.match_list,
			"finished": self.finished
		}
		return serialized_round


def unserialize(tournament_id, round_number):
	tournament = models.tournament.unserialize(tournament_id)
	round = tournament.rounds_list[round_number-1]
	return Round(
		name=round["name"],
		start_date=round["start_date"],
		end_date=round["end_date"],
		match_list=tournament["match_list"],
		finished=tournament["finished"]
	)


if __name__ == "__main__":
	pass
