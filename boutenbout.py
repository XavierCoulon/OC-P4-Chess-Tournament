from controllers.main_controller import db, User, table_players, table_tournament
import models.tournament
from models.round import Round, deserialize_round
from models.match import Match, deserialize


def main():




	tournament_name = "Christophe"
	tournament = models.tournament.deserialize_tournament(tournament_name)
	round = models.round.deserialize_round(tournament_name)
	print(round.match_list[-1])
	print(round.match_list)


	#matches = round.match_list
	# for match in matches:
	# 	print(match)
	# 	choice = input(f"Result match 'player {match[0][0]} vs player {match[1][1]}' (1/N/2): ")
	# 	if choice == "1":
	# 		match[0][1] = 1
	# 		match[1][1] = 0
	# 	elif choice == "N":
	# 		match[0][1] = 0.5
	# 		match[1][1] = 0.5
	# 	else:
	# 		match[0][1] = 0
	# 		match[1][1] = 1

	tournament.rounds_list[-1] = round.serialize()
	tournament.save()


	# tournament.add_players([1, 2, 3, 4, 5, 6, 7, 8])
	# new_round = Round()
	# tournament.rounds_list = (new_round.first_pairing(tournament_name).serialize())
	# tournament.save()


	# tournament = models.tournament.deserialize_round(tournament_name)
	# round = models.round.deserialize_round(tournament_name, 1)
	# liste = []
	# for element in round.match_list:
	# 	match = models.match.deserialize_round(element)
	# 	choice = input(f"Result match 'player {match.player1_id} vs player {match.player2_id}' (1/N/2): ")
	# 	if choice == "1":
	# 		match.result(1, 0)
	# 	elif choice == "N":
	# 		match.result(0.5, 0.5)
	# 	else:
	# 		match.result(0, 1)
	#
	# 	liste.append(match.serialize())
	# round.match_list = liste
	# tournament.rounds_list = [round.serialize()]
	# tournament.save()


if __name__ == "__main__":
	main()
