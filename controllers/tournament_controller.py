""" Controller managing Tournaments (including rounds and matches) """

import re
import controllers.home_controller
from controllers.main_controller import Controller, stop, MAX_ROUNDS_NUMBER, table_tournament, User, table_players
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from views.home_view import HomeView
from views.tournament_view import TournamentsView


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
				while not re.search('^\\d\\d/\\d\\d/\\d\\d$', date):
					date = self.view.invalid_format()
				game_type = self.view.prompt_for_game_type()
				while game_type.upper() not in ["RAPID", "BULLET", "BLITZ"]:
					game_type = self.view.invalid_format()
				description = self.view.prompt_for_description()

				new_tournament = Tournament(
					name=name,
					location=location,
					dates=date,
					game_type=game_type,
					description=description
					)
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
				prompt = TournamentsView.prompt_for_selecting_tournament()
				# Check if tournament exists in database
				if not table_tournament.get(User.name == prompt):
					self.view.tournament_not_found()
				else:
					tournament = Tournament.deserialize(prompt)
					if not tournament.players_list:
						self.view.players_missing()
					else:
						if len(tournament.rounds_list) == MAX_ROUNDS_NUMBER:
							self.view.rounds_limit_reached()
							break
						else:
							new_round = Round.deserialize(prompt)
							tournament.rounds_list += [new_round.create_round(prompt).serialize()]
							tournament.save()

			# Result matches of the last Round
			elif choice == "4":
				prompt = TournamentsView.prompt_for_selecting_tournament()
				tournament = Tournament.deserialize(prompt)
				tour = Round.deserialize(prompt)
				new_match_list = []
				for match in tour.match_list:
					match_instance = Match.deserialize(match)
					result = TournamentsView.prompt_for_resulting(
						match_instance.player1_id,
						match_instance.player2_id,
						match_instance.player1_name,
						match_instance.player2_name
					)
					tournament.update_global_score(match_instance.result(result, tournament))
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
				stop()
			else:
				pass


if __name__ == "__main__":
	pass
