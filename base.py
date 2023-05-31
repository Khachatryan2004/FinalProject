import random


class Shooter:
    def __init__(self, name, age, experience):
        self.name = name
        self.age = age
        self.experience = experience


class Novice(Shooter):
    def __init__(self, name, age, experience, probability):
        Shooter.__init__(self, name, age, experience)
        self.probability = probability

    def fire(self):
        self.probability = 0.01 * self.experience > random.uniform(0, 1)
        return self.probability


class Experienced(Shooter):
    def __init__(self, name, age, experience, probability):
        Shooter.__init__(self, name, age, experience)
        self.probability = probability

    def fire(self):
        self.probability = 0.05 * self.experience > random.uniform(0, 0.5)
        return self.probability


class Expert(Shooter):
    def __init__(self, name, age, experience, probability):
        Shooter.__init__(self, name, age, experience)
        self.probability = probability

    def fire(self):
        self.probability = 0.09 - 0.01 * self.age > random.uniform(-0.20, 0)
        return self.probability
