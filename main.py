""" Chess Tournament - main.py"""
import controllers.main_controller
import controllers.home_controller
from views.home_view import HomeView


def main():
	""" Main function"""
	app = controllers.home_controller.HomeController()
	app.start(HomeView)


if __name__ == "__main__":
	main()
