import random
import time
from copy import deepcopy

class state:
    def __init__(self, config):
        self.config = config

    def array_init(self):
        arr = [[0 for j in range(len(self.config))] for i in range(len(self.config))]
        for i, j in enumerate(self.config):
            arr[i][j] = 1
        return arr

    def column_checker(self, arr, i, j):
        cost = 0
        for p in range(len(arr[0])):
            if p == i:
                continue
            cost += arr[p][j]
        return cost

    def helper1(self, arr, i, j):
        cost = 0
        l = len(arr[0])
        m , n = i-1, j+1
        while m >= 0 and n < l:
            cost += arr[m][n]
            m -= 1
            n += 1
        m, n = i+1, j-1
        while m < l and n >= 0:
            cost += arr[m][n]
            m += 1
            n -= 1
        return cost

    def helper2(self, arr, i, j):
        cost = 0
        l = len(arr[0])
        m , n = i-1, j-1
        while m >= 0 and n >= 0:
            cost += arr[m][n]
            m -= 1
            n -= 1
        m, n = i+1, j+1
        while m < l and n < l:
            cost += arr[m][n]
            m += 1
            n += 1
        return cost

    def fitness(self):
        arr = self.array_init()
        cost = 0
        for i, j in enumerate(self.config):
            col = self.column_checker(arr, i, j)
            ud = self.helper2(arr, i, j)
            ld = self.helper1(arr, i, j)
            cost += col + ud + ld
        cost //= 2
        return -cost


def crossover(s1, s2):
    ran = random.randrange(0, 8)
    newconfig = []
    for i in range(9):
        if i < ran:
            newconfig.append(s1.config[i])
        else:
            newconfig.append(s2.config[i])
    return state(newconfig)

def mutation(s, rate):
    if random.random() <= rate:
        s.config[random.randrange(0, 8)] = random.randrange(0, 8)
    return s

def random_state():
    config = [random.randint(0,8) for i in range(9)]
    return config

def crossover(s1, s2, rate = 0.7):
    child = crossover(s1, s2)
    child = mutation(child, rate)
    return child


def geneticalgo():
    initial_gen = []
    for i in range(10):
        initial_gen.append(state(random_state()))
    
    next_gen = []
    while True:
        found = False
        for i in initial_gen:
                if i.fitness() == 0:
                    print("RESULT: ", i.config)
                    found = True
                    break
        
        if found == True:
            break
        
        initial_gen.sort(key = lambda x: x.fitness(), reverse = True)
        next_gen = initial_gen[:5]
        for i in range(5):
            next_gen.append(crossover(initial_gen[i], initial_gen[i + 1]))
        next_gen.append(state(random_state()))
        initial_gen = deepcopy(next_gen)

geneticalgo()

'''
RESULT found:  [4, 2, 7, 3, 1, 8, 5, 0, 6]
'''
        


        

        


        
        



    



