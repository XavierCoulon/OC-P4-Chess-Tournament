import controllers.home_controller
from controllers.main_controller import Controller, stop, MAX_ROUNDS_NUMBER
from models.tournament import Tournament
from models.round import Round
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
						tournament.rounds_list += [new_round.first_pairing(prompt).serialize()]
						tournament.save()
			elif choice == 4:
				prompt = TournamentsView.prompt_for_selecting_tournament()
				tournament = Tournament.deserialize(prompt)
				tour = Round.deserialize(prompt)
				tour.result_match()
				tournament.rounds_list[-1] = tour.serialize()
				tournament.save()
			elif choice == 5:
				self.controller = controllers.home_controller.HomeController()
				self.controller.start(HomeView)
			else:
				stop()


if __name__ == "__main__":
	pass
