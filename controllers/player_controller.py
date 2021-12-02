""" Controller managing Players """

import controllers.home_controller
import re
from datetime import datetime
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
				first_name = self.view.prompt_for_first_name()
				last_name = self.view.prompt_for_last_name()
				ranking = self.view.prompt_for_ranking()
				while True:
					try:
						ranking = int(ranking)
					except ValueError:
						ranking = self.view.invalid_format()
					else:
						break
				birth_date = self.view.prompt_for_birth_date()
				while not re.search('^\\d\\d/\\d\\d/\\d\\d$', birth_date):
					birth_date = self.view.invalid_format()
				gender = self.view.prompt_for_gender()
				while gender not in ["F", "M"]:
					gender = self.view.invalid_format()
				description = self.view.prompt_for_description()

				new_player = Player(
					first_name=first_name,
					last_name=last_name,
					gender=gender,
					ranking=ranking,
					birth_date=birth_date,
					description=description)
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
			elif choice == "q":
				stop()
			else:
				pass


if __name__ == "__main__":
	pass
