class TestView:

	def __init__(self):
		self.view = None

	def prompt_for_players(self):
		number = input("How many players do you want to create? ")
		return int(number)
