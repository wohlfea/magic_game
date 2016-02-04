import random
from combat import Combat


class Character(Combat):
    attack_limit = 10
    experience = 0
    base_points = 10
    def attack(self):
        roll = random.randint(1, self.attack_limit)
        if self.weapon == 'sword':
            roll += 1
        elif self.weapon == 'axe':
            roll += 2
        return roll > 4
    def get_weapon(self):
        weapon_choice = raw_input('Weapon ([S]word, [A]xe, [B]ow): ')
        if weapon_choice in 'sab':
            if weapon_choice.lower() == 's':
                return 'sword'
            elif weapon_choice.lower() == 'a':
                return 'axe'
            elif weapon_choice.lower() == 'b':
                return 'bow'
        else:
            return self.get_weapon()

    def __init__(self, **kwargs):
        self.name = raw_input('Name: ')
        self.weapon = self.get_weapon()
        self.hit_points = self.base_points

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return '{}, HP: {}, XP: {}'.format(self.name, self.hit_points, self.experience)

    def rest(self):
        if self.hit_points < self.base_points:
            self.hit_points += 1
            return True
        else:
            return False

    def leveled_up(self):
        return self.experience >= 5
