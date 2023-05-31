from base import Shooter
import random


class Expert(Shooter):
    def __init__(self, name, age, experience, probability):
        Shooter.__init__(self, name, age, experience)
        self.probability = probability

    def fire(self):
        self.probability = 0.09 - 0.01 * self.age > random.uniform(-0.04, 0)
        return self.probability
