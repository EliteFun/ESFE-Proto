from . import state_manager

import pygame


class Game:

    def __init__(self, videomode,
                 title, framerate,
                 clearColor):

        pygame.init()

        self.window = pygame.display.set_mode(videomode)
        pygame.display.set_caption(title)

        self.clearColor = clearColor
        self.framerate = framerate

        self.state_manager = state_manager.StateManager()

    def gameLoop(self):
        clock = pygame.time.Clock()

        while True:
            elapsed = clock.tick(self.framerate)

            for event in pygame.event.get():
                self.state_manager.onEvent(event)

            self.state_manager.update(elapsed)

            self.window.fill(self.clearColor)
            self.state_manager.draw(elapsed)
            pygame.display.flip()
