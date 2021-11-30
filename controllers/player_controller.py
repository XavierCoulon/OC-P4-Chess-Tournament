""" Controller managing Players """

import controllers.home_controller
from controllers.main_controller import Controller, stop, table_players
from models.player import Player
from views.home_view import HomeView


class PlayersController(Controller):
	""" Class for Player controller"""
	def run(self):
		""" Run the controller"""
		while self.controller:
			choice = self.view.display_menu()

			# Manual creation of a player
			if choice == "1":
				player = self.view.prompt_for_manual_creation_player()
				new_player = Player(
					first_name=player[0],
					last_name=player[1],
					ranking=int(player[2]),
					birth_date=player[3],
					gender=player[4],
					description=player[5])
				new_player.__str__()
				new_player.save()

			# Update the ranking of a player
			elif choice == "2":
				result = self.view.prompt_for_update_ranking()
				# If player does not exist in database
				if not table_players.get(doc_id=int(result[0])):
					self.view.player_not_found()
				else:
					player = Player.deserialize(int(result[0]))
					player.update_ranking(int(result[1]))
					player.__str__()
					player.save()

			# Back to Home menu
			elif choice == "3":
				self.controller = controllers.home_controller.HomeController()
				self.controller.start(HomeView)

			# To generate automatically players
			# (not displayed on the user's interface)
			elif choice == "a":
				number = self.view.prompt_for_how_many_players()
				for player in range(int(number)):
					new_player = Player()
					new_player.auto_creation()
					new_player.__str__()
					new_player.save()
			else:
				stop()


if __name__ == "__main__":
	pass
