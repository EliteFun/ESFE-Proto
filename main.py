import pygame
import sys
from ESFE.Util import game, state

game = game.Game((800, 600), "hi", 60, pygame.Color(255, 255, 255, 255))


class GameState(state.State):
    def __init__(self):
        pass

    def onEvent(self, e):
        if e.type == pygame.QUIT:
            sys.exit()


game_state = GameState()

game.state_manager.pushState(game_state)
game.gameLoop()
