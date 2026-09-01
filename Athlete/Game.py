import random
from Team import Team
from Sport import Sport
from Athlete import Athlete

class Game:

    def __init__(self, A:Team, B:Team):

        self.team_A = A
        self.team_B = B
        self.socre = {self.team_A: 0, self.team_B: 0}

    def play(self):

        a = random.randint(0, 100)
        b = random.randint(0, 100)
        

        