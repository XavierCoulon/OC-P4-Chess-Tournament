import controllers.home_controller
from controllers.main_controller import Controller, db, stop
from models.tournament import Tournament, deserialize_tournament
from models.round import Round, deserialize_round
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
			elif choice == 2:
				new_tournament = Tournament()
				new_tournament.auto_creation()
				new_tournament.save()
			elif choice == 3:
				self.view.display_tournaments_db(db)
			elif choice == 4:
				choice = self.view.prompt_for_allocating_players()
				tournament = deserialize_round(choice[0])
				tournament.add_players(choice[1])
				tournament.save()
			elif choice == 5:
				prompt = TournamentsView.prompt_for_selecting_tournament()
				tournament = deserialize_tournament(prompt)
				new_round = deserialize_round(prompt)
				tournament.rounds_list += [new_round.first_pairing(prompt).serialize()]
				tournament.save()
				TournamentsView.prompt_for_round_created()
			elif choice == 6:
				prompt = TournamentsView.prompt_for_selecting_tournament()
				tournament = deserialize_tournament(prompt)
				round = deserialize_round(prompt)
				round.result_match()
				tournament.rounds_list[-1] = round.serialize()
				tournament.save()
			elif choice == 7:
				self.controller = controllers.home_controller.HomeController()
				self.controller.start(HomeView)
			else:
				stop()


if __name__ == "__main__":
	pass
