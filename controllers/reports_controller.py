""" Controller managing Reports """

import controllers.home_controller
import views.reports_view
from controllers.main_controller import Controller, stop, User
from controllers.main_controller import table_tournament, table_players
from views.home_view import HomeView
from views.tournament_view import TournamentsView
from views.reports_view import ReportsView
from models.match import Match


class ReportsController(Controller):
	""" Classe for Reports' controller"""
	def run(self):
		""" Run controller """
		while self.controller:
			choice = self.view.display_menu()

			# Cf. Reports view for matching
			if choice == "1":
				ReportsView.display_players(self.all_players("r"))
			elif choice == "2":
				ReportsView.display_players(self.all_players("a"))
			elif choice in ["3", "4", "5", "7", "8"]:
				tournament_name = TournamentsView.prompt_for_selecting_tournament()
				if not table_tournament.get(User.name == tournament_name):
					views.reports_view.ReportsView.tournament_not_found()
				else:
					if choice == "3":
						ReportsView.display_players_score(self.players_tournament(tournament_name, "r"))
					elif choice == "4":
						ReportsView.display_players_score(self.players_tournament(tournament_name, "a"))
					elif choice == "5":
						ReportsView.display_players_score(self.players_tournament(tournament_name, "s"))
					elif choice == "7":
						ReportsView.display_rounds(self.all_rounds(tournament_name), tournament_name)
					else:
						self.all_matches(tournament_name)
			elif choice == "6":
				ReportsView.display_tournaments(self.all_tournaments())
			elif choice == "9":
				self.controller = controllers.home_controller.HomeController()
				self.controller.start(HomeView)
			elif choice in ["q", "10"]:
				stop()
			else:
				pass

	@staticmethod
	def players_tournament(tournament_name, sort):
		""" Players' tournament list, sorted by ranking or alphabetical order

		Args:
			tournament_name (str): name of the tournament
			sort (str): "r" for ranking, any other key for alphabetical order

		Returns:
			players' list (list)
		"""
		players = table_tournament.get(User.name == tournament_name).get("players_list")
		players_data = []
		for player in players:
			player_data = (
				player,
				table_players.get(doc_id=int(player)).get("last_name"),
				table_players.get(doc_id=int(player)).get("first_name"),
				table_players.get(doc_id=int(player)).get("ranking"),
				players.get(player)
			)
			players_data.append(player_data)
		players_list_by_alph = sorted(players_data, key=lambda x: x[1])
		players_list_by_ranking = sorted(players_data, key=lambda x: x[3])
		players_list_by_score = sorted(players_data, reverse=True, key=lambda x: (x[4], -x[3]))
		if sort == "r":
			return players_list_by_ranking
		elif sort == "a":
			return players_list_by_alph
		else:
			return players_list_by_score

	@staticmethod
	def all_players(sort):
		""" All players sorted by alphabetical order

		Args:
			sort (str): "r" for ranking, any other key for alphabetical order

		Returns:
			players' list (list)
		"""
		players_data = []
		# get players from database
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
		""" All tournaments sorted by alphabetical order

		Returns:
			tournaments' list (list)
		"""

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
		""" All rounds of a tournament

		Args:
			tournament_name (str): name of a tournament

		Returns:
			Rounds' list (list)
		"""

		rounds = table_tournament.get(User.name == tournament_name).get("rounds_list")
		rounds_data = []
		for tour in rounds:
			round_data = [
				tour.get("name"),
				tour.get("start_date"),
				tour.get("end_date"),
				tour.get("finished")
			]
			rounds_data.append(round_data)
		return sorted(rounds_data, key=lambda x: x[0])

	@staticmethod
	def all_matches(tournament_name):
		""" All players sorted by alphabetical order (use of __str__ on Match to display)

		Args:
			tournament_name (str): name of a tournament

		"""
		rounds_list = table_tournament.get(User.name == tournament_name).get("rounds_list")
		for tour in rounds_list:
			for match in tour["match_list"]:
				Match.deserialize(match).__str__()


if __name__ == "__main__":
	pass
