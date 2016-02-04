import sys
import os
from character import Character
from monster import Goblin
from monster import Dragon
from monster import Troll


class Game:
    def set_up(self):
        os.system('clear')
        self.player = Character()
        self.monsters = [
            Goblin(),
            Troll(),
            Dragon()
        ]
        self.monster = self.get_next_monster()

    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        print('=========================')
        print(self.player.__str__())
        print('=========================')
        print(self.monster.__str__())
        print('=========================')
        if self.monster.attack():
            print('A {} has attacked you'.format(self.monster.name))
            dodge_decide = raw_input('Would you like to dodge? [y/n] ')
            if dodge_decide.lower() == 'y':
                if self.player.dodge():
                    print('You successfully dodged the attack!')
                else:
                    print('Your dodge was unsuccessful. You were hit by a {} and took 1 damage.'.format(self.monster.name))
                    self.player.hit_points += -1
            else:
                print('You decided not to dodge and were hit by a {}. You took 1 damage.'.format(self.monster.name))
                self.player.hit_points += -1
        else:
            print('The {} missed his attack! You took 0 damage!'.format(self.monster.name))

    def player_turn(self):
        print('=========================')
        print(self.player.__str__())
        print('=========================')
        print(self.monster.__str__())
        print('=========================')
        print('It\'s now your turn {}. What do you decide?'.format(self.player.name))
        choice = raw_input('You can [A]ttack, [R]est, or [Q]uit the game. ')
        if choice.lower() == 'a':
            print('You have decided to attack!')
            if self.player.attack():
                print('You attack and the {} attempts to dodge.'.format(self.monster.name))
                if self.monster.dodge():
                    print('The {} successfully dodged your attack. You missed!'.format(self.monster.name))
                else:
                    print('The {}\'s attempted to dodge but was unsuccessful! You hit the {} for 1 damage.'.format(self.monster.name, self.monster.name))
                    self.monster.hit_points += -1
            else:
                print('You tried to attack but missed!')
        elif choice.lower() == 'r':
            print('You have decided to rest.')
            if self.player.rest():
                print('You recovered 1 hp from resting.')
            else:
                print('You are already full health. You don\'t need to rest')
        elif choice.lower() == 'q':
            print('Thank you for playing.')
            sys.exit()
        else:
            print('Your selection was invalid. Please try again...')
            self.player_turn()

    def cleanup(self):
        if self.monster.hit_points <= 0:
            print('You have slain the {}. You gained 5 experience points.'.format(self.monster.name))
            self.player.experience += self.monster.experience
            self.monster = self.get_next_monster()
            if self.monster:
                print('A wild {} appears! He doesn\'t look happy!'.format(self.monster.name))

    def game_continue(self):
        pause = raw_input('Press Enter/Return to continue... ')
        os.system('clear')

    def __init__(self):
        self.set_up()
        while self.player.hit_points and (self.monster or self.monsters):
            self.game_continue()
            self.monster_turn()
            self.game_continue()
            self.player_turn()
            self.cleanup()
        if self.player.hit_points:
            print('You win!!!!')
        elif self.monster or self.monsters:
            print('You lose!!!')
        sys.exit()


newGame = Game()
