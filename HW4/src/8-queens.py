import random

num = 5
states = []

for n in range(num):
    states.append([random.randrange(1, 9, 1) for i in range(8)])

initial = [5, 6, 7, 4, 5, 6, 7, 6]
def hill_climbing(state):
    attacks = 0;

    for i in state:
        for j in state:
            print(f'i {state[i]}')

    


hill_climbing(initial)