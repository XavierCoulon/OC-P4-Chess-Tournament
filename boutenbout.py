from controllers.main_controller import table_tournament, User, table_players
from models.round import Round


def main():
	tournament = table_tournament.get(User.name == "qsdcqdsc")
	print(tournament)


if __name__ == "__main__":
	main()
