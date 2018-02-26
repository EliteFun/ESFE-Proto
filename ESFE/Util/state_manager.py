class StateManager:

    def __init__(self):
        self.states = []

    def popState(self):
        if self.states:
            self.states.pop()

    def changeState(self, state):
        if self.states:
            self.states.pop()

        self.states.append(state)

    def pushState(self, state):
        self.states.append(state)

    def onEvent(self, e):
        self.states[-1].onEvent(e)

    def update(self, dt):
        self.states[-1].update(dt)

    def draw(self, dt):
        self.states[-1].draw(dt)
