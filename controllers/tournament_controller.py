import controllers.home_controller
from controllers.main_controller import Controller, db, stop
from models.tournament import Tournament
from views.views import HomeView


class TournamentsController(Controller):

	def run(self):
		while self.controller:
			choice = self.view.display_menu()
			if choice == 1:
				new_tournament = Tournament()
				new_tournament.auto_creation()
				new_tournament.save(new_tournament.serialize())
			elif choice == 2:
				self.view.display_tournaments_db(db)
			elif choice == 3:
				self.controller = controllers.home_controller.HomeController()
				self.controller.start(HomeView)
			else:
				stop()


if __name__ == "__main__":
	pass


