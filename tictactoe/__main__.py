from .CLIFrontend import CLIFrontend
from .Game import Game

game = Game()
frontend = CLIFrontend(game)
frontend.main()