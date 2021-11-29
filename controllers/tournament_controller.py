import controllers.home_controller
import views.reports_view
from controllers.main_controller import Controller, stop, MAX_ROUNDS_NUMBER, table_tournament
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from views.home_view import HomeView
from views.tournament_view import TournamentsView


class TournamentsController(Controller):

	def run(self):
		while self.controller:
			choice = self.view.display_menu()
			if choice == 1:
				tournament = self.view.prompt_for_manual_creation_tournament()
				new_tournament = Tournament(
					name=tournament[0],
					location=tournament[1],
					dates=tournament[2],
					game_type=tournament[3],
					description=tournament[4])
				new_tournament.save()
			elif choice == 7:
				new_tournament = Tournament()
				new_tournament.auto_creation()
				new_tournament.save()
			elif choice == 2:
				choice = self.view.prompt_for_allocating_players()
				if not table_tournament.get(doc_id=choice[0]):
					self.view.tournament_not_found()
				else:
					tournament = Tournament.deserialize(choice[0])
					tournament.add_players(choice[1])
					self.view.allocated_players()
					tournament.save()
			elif choice == 3:
				prompt = TournamentsView.prompt_for_selecting_tournament()
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
			elif choice == 4:
				prompt = TournamentsView.prompt_for_selecting_tournament()
				tournament = Tournament.deserialize(prompt)
				tour = Round.deserialize(prompt)
				new_match_list = []
				for match in tour.match_list:
					match_instance = Match.deserialize(match)
					result = TournamentsView.prompt_for_resulting(match_instance.player1_id, match_instance.player2_id)
					match_instance.result(result, tournament)
					new_match_list.append(match_instance.serialize())
				tour.match_list = new_match_list
				tour.close()
				tournament.rounds_list[-1] = tour.serialize()
				tournament.save()
			elif choice == 5:
				self.controller = controllers.home_controller.HomeController()
				self.controller.start(HomeView)
			else:
				stop()


if __name__ == "__main__":
	pass
