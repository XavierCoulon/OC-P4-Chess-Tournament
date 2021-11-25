from controllers.main_controller import db, User, table_players, table_tournament
import models.tournament
from models.round import Round, deserialize_round
from models.match import Match, deserialize


def main():

	# last round
	last_round = [['6', 2, 4], ['1', 1.5, 11], ['2', 0.5, 14], ['4', 0, 13]]

	#new_round = [[x, y] for (x, y) in zip(last_round, last_round)]

	liste = []
	for x, y in zip(*[iter(last_round)] * 2):
		liste.append([x, y])

	print(liste)





if __name__ == "__main__":
	main()
