import models.round
from models.tournament import Tournament, add_players, unserialize_tournament
from models.round import Round, unserialize
from models.match import Match, unserialize


def main():
	add_players("Virginie", [1, 2, 3, 4, 5, 6, 7, 8])
	tournament = unserialize_tournament("Virginie")
	new_round = Round()
	tournament.rounds_list = [new_round.first_pairing("Virginie")]
	tournament.save(tournament.serialize())

	tournament = unserialize_tournament("Virginie")
	round = models.round.unserialize("Virginie", 1)
	liste = []
	for element in round.match_list:
		match = unserialize(element)
		match.result(1, 0)
		liste.append(match.serialize())
	round.match_list = liste
	tournament.rounds_list = [round.serialize()]
	tournament.save(tournament.serialize())


if __name__ == "__main__":
	main()
