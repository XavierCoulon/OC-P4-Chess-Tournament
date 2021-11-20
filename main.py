import controllers.main_controller
import controllers.home_controller
from views.views import HomeView


def main():
	game = controllers.home_controller.HomeController()
	game.start(HomeView)


if __name__ == "__main__":
	main()
