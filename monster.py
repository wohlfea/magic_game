import random
from combat import Combat


COLORS = ['Blue', 'Black', 'Yellow', 'Green', 'Red']


class Monster(Combat):
    min_hit_points = 1
    max_hit_points = 1
    min_experience = 1
    max_experience = 1
    weapon = 'sword'
    sound = 'roar'

    def __init__(self, **kwargs):
        self.name = self.__class__.__name__
        self.hit_points = random.randint(
                                         self.min_hit_points,
                                         self.max_hit_points
                                         )
        self.experience = random.randint(
                                         self.min_experience,
                                         self.max_experience
                                         )
        self.color = random.choice(COLORS)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return'{} {}, HP: {}, XP: {}'.format(
                                             self.color,
                                             self.__class__.__name__,
                                             self.hit_points,
                                             self.experience
                                             )

    def battlecry(self):
        return self.sound.upper()


class Goblin(Monster):
    min_hit_points = 2
    max_hit_points = 3
    min_experience = 2
    max_experience = 3
    sound = 'squeak'


class Troll(Monster):
    min_hit_points = 4
    max_hit_points = 5
    min_experience = 4
    max_experience = 5
    sound = 'glargh'


class Dragon(Monster):
    min_hit_points = 7
    max_hit_points = 10
    min_experience = 7
    max_experience = 10
    sound = 'raaaarrrrr'
