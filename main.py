from model import SushiMenu
from view import ConsoleView
from controller import SushiController

# Запуск програми
if __name__ == "__main__":
    model = SushiMenu()
    view = ConsoleView(model)
    controller = SushiController(model, view)
    controller.run()