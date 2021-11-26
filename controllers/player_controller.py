import controllers.home_controller
from controllers.main_controller import Controller, db, stop
from models.player import Player
from views.home_view import HomeView


class PlayersController(Controller):

	def run(self):
		while self.controller:
			choice = self.view.display_menu()
			if choice == 1:
				player = self.view.prompt_for_manual_creation_player()
				new_player = Player(
					first_name=player[0],
					last_name=player[1],
					ranking=int(player[2]),
					birth_date=player[3],
					gender=player[4],
					description=player[5])
				new_player.save()
			elif choice == 2:
				number = self.view.prompt_for_how_many_players()
				for player in range(int(number)):
					new_player = Player()
					new_player.auto_creation()
					new_player.save()
			elif choice == 3:
				self.view.display_players_db(db)
			elif choice == 4:
				result = self.view.prompt_for_update_ranking()
				player = Player.deserialize(int(result[0]))
				player.update_ranking(int(result[1]))
				player.save()
			elif choice == 5:
				self.controller = controllers.home_controller.HomeController()
				self.controller.start(HomeView)
			else:
				stop()


if __name__ == "__main__":
	pass
