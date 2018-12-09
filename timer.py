import time
# Simple timer class
# Adapted from https://stackoverflow.com/questions/39883175/game-timer-in-pygame
class Timer:
    def __init__(self):
        self.elapsed = 0.0
        self.run = False
        self.last = None

    def start(self):
        if not self.running:
            self.run = True
            self.last = time.time()

    def pause(self):
        if self.run:
            self.run = False
            self.elapsed += time.time() - self.last

    def get_elapsed(self):
        elapsed = self.elapsed
        if self.run:
            elapsed += time.time() - self.last
        return elapsed
