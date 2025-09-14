import random
import seaborn as sns


class Gym:
    def __init__(self):
        self.dumbbells = [i for i in range(10,50) if i%2==0]
        self.places = {}
        self.reboot()

    def reboot(self):
        self.places = {i: i for i in self.dumbbells}

    def list_dumbbells(self):
        return [i for i in self.places.values() if i != 0]
    
    def list_places(self):
        return [i for i, j in self.places.items() if j == 0]
    
    def take_dumbbell(self, dumbbell):
        dumbbell_pos = list(self.places.values()).index(dumbbell)
        key_dumbbell = list(self.places.keys())[dumbbell_pos]
        self.places[key_dumbbell] = 0
        return dumbbell
    
    def return_dumbbell(self, pos, dumbbell):
        self.places[pos] = dumbbell

    def calculate_chaos(self):
        num_chaos = [i for i, j in self.places.items() if i != j]
        return len(num_chaos)/len(self.places)

class User:
    def __init__(self, type, gym):
        self.type = type # type 1: normal, type 2: messy
        self.gym = gym
        self.dumbbell = 0

    def init_exercise(self):
        list_dumbbells = self.gym.list_dumbbells()
        self.dumbbell = random.choice(list_dumbbells)
        self.gym.take_dumbbell(self.dumbbell)

    def finish_exercise(self):
        places = self.gym.list_places()

        if self.type == 1:
            if self.dumbbell in places:
                self.gym.return_dumbbell(self.dumbbell, self.dumbbell)
            else:
                pos = random.choice(places)
                self.gym.return_dumbbell(pos, self.dumbbell)

        elif self.type == 2:
            pos = random.choice(places)
            self.gym.return_dumbbell(pos, self.dumbbell)
        
        self.dumbbell = 0

gym = Gym()

users = [User(1,gym) for i in range(20)]
users += [User(2,gym) for i in range(1)]
random.shuffle(users)

list_chaos = []

for k in range(50):
    for i in range(10):
        random.shuffle(users)
        for user in users:
            user.init_exercise()
        for user in users:
            user.finish_exercise()
    list_chaos += [gym.calculate_chaos()]

sns.displot(list_chaos)
