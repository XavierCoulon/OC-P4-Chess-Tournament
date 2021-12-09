""" Controller managing Tournaments (including rounds and matches) """

import controllers.home_controller
from datetime import datetime
from controllers.main_controller import Controller, table_tournament, User, table_players
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from views.home_view import HomeView
from views.tournament_view import TournamentsView

# Limit of rounds by default
MAX_ROUNDS_NUMBER = 4


class TournamentsController(Controller):
	""" Class for Tournament Controller"""
	def run(self):
		""" Run the controller"""
		while self.controller:
			choice = self.view.display_menu()

			# Manual creation of a tournament
			if choice == "1":
				name = self.view.prompt_for_name()
				location = self.view.prompt_for_location()
				date = self.view.prompt_for_date()
				# Check date format
				while True:
					try:
						datetime.strptime(date, "%d/%m/%y")
					except ValueError:
						date = self.view.invalid_format()
					else:
						break
				game_type = self.view.prompt_for_game_type()
				# Check game type
				while game_type.upper() not in ["RAPID", "BULLET", "BLITZ"]:
					game_type = self.view.invalid_format()
				description = self.view.prompt_for_description()

				new_tournament = Tournament(
					name=name,
					location=location,
					dates=date,
					game_type=game_type,
					description=description)
				new_tournament.__str__()
				new_tournament.save()

			# Allocate players to a tournament
			elif choice == "2":
				choice = self.view.prompt_for_allocating_players()
				# Check if tournament exists in database
				if not table_tournament.get(User.name == choice[0]):
					self.view.tournament_not_found()
					return
				else:
					players = choice[1]
					if len(players) % 2 != 0:
						self.view.uneven_players()
						break
					for player in players:
						try:
							player = int(player)
						except ValueError:
							self.view.player_not_found(player)
							return
						if not table_players.get(doc_id=int(player)):
							self.view.player_not_found(player)
							return
					tournament = Tournament.deserialize(choice[0])
					tournament.add_players(players)
					self.view.allocated_players()
					tournament.save()

			# Create a new round
			elif choice == "3":
				tournament_name = TournamentsView.prompt_for_selecting_tournament()
				# Check if tournament exists in database
				if not table_tournament.get(User.name == tournament_name):
					self.view.tournament_not_found()
				else:
					tournament = Tournament.deserialize(tournament_name)
					last_round = Round.deserialize(tournament_name)
					if not tournament.players_list:
						self.view.players_missing()
						break
					elif len(tournament.rounds_list) == MAX_ROUNDS_NUMBER:
						self.view.rounds_limit_reached()
						break
					elif tournament.rounds_list and not last_round.end_date:
						self.view.last_round_not_resulted()
						break
					else:
						tournament.rounds_list += [last_round.create_round(tournament_name).serialize()]
						tournament.save()

			# Result matches of the last Round
			elif choice == "4":
				prompt = TournamentsView.prompt_for_selecting_tournament()
				# Check if tournament exists in database
				if not table_tournament.get(User.name == prompt):
					self.view.tournament_not_found()
				else:
					tournament = Tournament.deserialize(prompt)
					# If no round found in the tournament
					if not tournament.rounds_list:
						self.view.no_round_found()
						break
					tour = Round.deserialize(prompt)
					# If last round has already been resulted, warning and quit
					if tour.end_date:
						self.view.tournament_already_resulted()
						break
					new_match_list = []
					for match in tour.match_list:
						match_instance = Match.deserialize(match)
						result = TournamentsView.prompt_for_resulting(
							match_instance.player1_id,
							match_instance.player2_id,
							match_instance.player1_name,
							match_instance.player2_name
						)
						while result not in ["1", "N", "2"]:
							result = self.view.invalid_format()
						tournament.update_global_score(match_instance.result(result))
						new_match_list.append(match_instance.serialize())
					tour.match_list = new_match_list
					tour.close()
					tour.__str__()
					tournament.rounds_list[-1] = tour.serialize()
					tournament.save()

			# Back to Home menu
			elif choice == "5":
				self.controller = controllers.home_controller.HomeController()
				self.controller.start(HomeView)

			# To generate automatically a tournament (not displayed on the user's interface)
			elif choice == "a":
				new_tournament = Tournament()
				new_tournament.auto_creation()
				new_tournament.__str__()
				new_tournament.save()

			elif choice in ["q", "6"]:
				self.stop()
			else:
				pass


if __name__ == "__main__":
	pass
