""" Controller for Home menu"""

from controllers.player_controller import PlayersController
from controllers.tournament_controller import TournamentsController
from controllers.reports_controller import ReportsController
from views.tournament_view import TournamentsView
from views.reports_view import ReportsView
from views.player_view import PlayersView
from controllers.main_controller import Controller, stop


class HomeController(Controller):
	""" Class for Home controller"""
	def run(self):
		while self.controller:
			choice = self.view.display_menu()

			# Access to Players' menu
			if choice == "1":
				self.controller = PlayersController()
				self.controller.start(PlayersView)
			# Access to Tournaments' menu
			elif choice == "2":
				self.controller = TournamentsController()
				self.controller.start(TournamentsView)
			# Access to Reports' menu
			elif choice == "3":
				self.controller = ReportsController()
				self.controller.start(ReportsView)
			elif choice in ["q", "4"]:
				stop()
			else:
				pass


if __name__ == "__main__":
	pass
