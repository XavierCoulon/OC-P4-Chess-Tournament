from controllers.main_controller import db, User, table_players, table_tournament
from views.tournament_view import TournamentsView


def main():
	TournamentsView.display_players_tournament(2)


if __name__ == "__main__":
	main()
