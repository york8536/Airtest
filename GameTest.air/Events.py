class Events:
    def __init__(self):
        self.listeners = {}

    def emit(self, event, *args):
        if event in self.listeners:
            for listener in self.listeners[event]:
                listener(*args)

    def on(self, event, listener):
        if event not in self.listeners:
            self.listeners[event] = []
        self.listeners[event].append(listener)