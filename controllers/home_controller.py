from controllers.player_controller import PlayersController
from controllers.tournament_controller import TournamentsController
from controllers.reports_controller import ReportsController
from views.tournament_view import TournamentsView
from views.reports_view import ReportsView
from views.player_view import PlayersView
from controllers.main_controller import Controller, stop


class HomeController(Controller):

	def run(self):
		while self.controller:
			choice = self.view.display_menu()
			if choice == 1:
				self.controller = PlayersController()
				self.controller.start(PlayersView)
			elif choice == 2:
				self.controller = TournamentsController()
				self.controller.start(TournamentsView)
			elif choice == 3:
				self.controller = ReportsController()
				self.controller.start(ReportsView)
			else:
				stop()


if __name__ == "__main__":
	print(HomeController())


