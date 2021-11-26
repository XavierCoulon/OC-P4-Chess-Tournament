import controllers.home_controller
from controllers.main_controller import Controller, stop, User
from controllers.main_controller import table_tournament, table_players
from views.home_view import HomeView
from views.tournament_view import TournamentsView
from views.reports_view import ReportsView


class ReportsController(Controller):

	def run(self):
		while self.controller:
			choice = self.view.display_menu()
			if choice == 1:
				ReportsView.display_players(self.all_players("r"))
			elif choice == 2:
				ReportsView.display_players(self.all_players("a"))
			elif choice == 3 or choice == 4:
				tournament_name = TournamentsView.prompt_for_selecting_tournament()
				if choice == 3:
					ReportsView.display_players(self.players_tournament(tournament_name, "r"))
				else:
					ReportsView.display_players(self.players_tournament(tournament_name, "a"))
			elif choice == 5:
				ReportsView.display_tournaments(self.all_tournaments())
			elif choice == 6:
				tournament_name = TournamentsView.prompt_for_selecting_tournament()
				ReportsView.display_rounds(self.all_rounds(tournament_name), tournament_name)
			elif choice == 7:
				tournament_name = TournamentsView.prompt_for_selecting_tournament()
				ReportsView.display_matches(self.all_matches(tournament_name), tournament_name)
			elif choice == 8:
				self.controller = controllers.home_controller.HomeController()
				self.controller.start(HomeView)
			else:
				stop()

	@staticmethod
	def players_tournament(tournament_name, sort):
		players = table_tournament.get(User.name == tournament_name).get("players_list")
		players_data = []
		for player in players:
			player_data = (
				player,
				table_players.get(doc_id=int(player)).get("last_name"),
				table_players.get(doc_id=int(player)).get("first_name"),
				table_players.get(doc_id=int(player)).get("ranking")
			)
			players_data.append(player_data)
		players_list_by_alph = sorted(players_data, key=lambda x: x[1])
		players_list_by_ranking = sorted(players_data, key=lambda x: x[3])

		if sort == "r":
			return players_list_by_ranking
		else:
			return players_list_by_alph

	@staticmethod
	def all_players(sort):
		players_data = []
		for player in table_players:
			player_data = [
				player.doc_id,
				player.get("last_name"),
				player.get("first_name"),
				player.get("ranking")
			]
			players_data.append(player_data)
		players_list_by_alph = sorted(players_data, key=lambda x: x[1])
		players_list_by_ranking = sorted(players_data, key=lambda x: x[3])

		if sort == "r":
			return players_list_by_ranking
		else:
			return players_list_by_alph

	@staticmethod
	def all_tournaments():
		tournaments = []
		for tournament in table_tournament:
			tournament_data = [
				tournament.get("name"),
				tournament.doc_id,
				tournament.get("players_list"),
				tournament.get("location"),
				tournament.get("game_type"),
				tournament.get("description")]
			tournaments.append(tournament_data)
		return sorted(tournaments, key=lambda x: x[0])

	@staticmethod
	def all_rounds(tournament_name):
		rounds = table_tournament.get(User.name == tournament_name).get("rounds_list")
		rounds_data = []
		for round in rounds:
			round_data = [
				round.get("name"),
				round.get("start_date"),
				round.get("end_date"),
				round.get("finished")
			]
			rounds_data.append(round_data)
		print(rounds_data)
		return sorted(rounds_data, key=lambda x: x[0])

	@staticmethod
	def all_matches(tournament_name):
		rounds_list = table_tournament.get(User.name == tournament_name).get("rounds_list")
		matches = []
		for round in rounds_list:
			matches.append(round.get("match_list"))
		return matches


if __name__ == "__main__":
	pass
