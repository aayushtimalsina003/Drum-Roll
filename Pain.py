from Enemy import *
import random

class Pain(Enemy):

    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy= 'Pain',
                         health_points= health_points,
                         attack_damage= attack_damage)

    def talk(self):
        print('The world shall know the pain...')

    def universal_destruction(self):
        print('The worlds gonna bear the pain I received')

    def special_attack(self):
        did_special_attack_work = random.random() < 0.10
        
