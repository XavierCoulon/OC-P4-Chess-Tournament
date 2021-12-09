""" Controller managing Players """

import controllers.home_controller
from datetime import datetime
from controllers.main_controller import Controller, table_players
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
				# Ranking must be an integer
				while True:
					try:
						ranking = int(ranking)
					except ValueError:
						ranking = self.view.invalid_format()
					else:
						break
				# Birth date format checked
				birth_date = self.view.prompt_for_birth_date()
				while True:
					try:
						datetime.strptime(birth_date, "%d/%m/%y")
					except ValueError:
						birth_date = self.view.invalid_format()
					else:
						break
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
				player_id = self.view.prompt_for_player_id()
				# Player ID has to be int
				try:
					int(player_id)
				except ValueError:
					self.view.player_not_found()
					break
				ranking = self.view.prompt_for_ranking()
				# Ranking has to be int
				while True:
					try:
						ranking = int(ranking)
					except ValueError:
						ranking = self.view.invalid_format()
					else:
						break
				# If player does not exist in database
				if not table_players.get(doc_id=int(player_id)):
					self.view.player_not_found()
				else:
					player = Player.deserialize(int(player_id))
					player.update_ranking(int(ranking))
					player.__str__()
					player.save()

			# Back to Home menu
			elif choice == "3":
				self.controller = controllers.home_controller.HomeController()
				self.controller.start(HomeView)

			# To generate automatically players (not displayed on the user's interface)
			elif choice == "a":
				number = self.view.prompt_for_how_many_players()
				for player in range(int(number)):
					new_player = Player()
					new_player.auto_creation()
					new_player.__str__()
					new_player.save()
			elif choice in ["q", "4"]:
				self.stop()
			else:
				pass


if __name__ == "__main__":
	pass
