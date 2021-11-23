import controllers.home_controller
import views.tournament_view
from controllers.main_controller import Controller, db, stop
from models.tournament import Tournament, add_players, unserialize_tournament
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
				new_tournament.save(new_tournament.serialize())
			elif choice == 2:
				new_tournament = Tournament()
				new_tournament.auto_creation()
				new_tournament.save(new_tournament.serialize())
			elif choice == 3:
				self.view.display_tournaments_db(db)
			elif choice == 4:
				choice = self.view.prompt_for_allocating_players()
				add_players(choice[0], choice[1])
			elif choice == 5:
				prompt = TournamentsView.prompt_for_selecting_tournament()
				tournament = unserialize_tournament(prompt)
				new_round = Round()
				tournament.rounds_list = [new_round.first_pairing(prompt)]
				tournament.save(tournament.serialize())
				TournamentsView.prompt_for_round_created()
			elif choice == 6:
				self.controller = controllers.home_controller.HomeController()
				self.controller.start(HomeView)
			else:
				stop()


if __name__ == "__main__":
	pass
