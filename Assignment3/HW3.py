# CptS 355 - Fall 2021 - Assignment 3
# Please include your name and the names of the students with whom you discussed any of the problems in this homework

from functools import reduce
debugging = False


def debug(*s):
    if debugging:
        print(*s)


my_cats_log = {(2, 2019): {"Oceanfish": 7, "Tuna": 1, "Whitefish": 3, "Chicken": 4, "Beef": 2},
               (5, 2019): {"Oceanfish": 6, "Tuna": 2, "Whitefish": 1, "Salmon": 3, "Chicken": 6},
               (9, 2019): {"Tuna": 3, "Whitefish": 3, "Salmon": 2, "Chicken": 5, "Beef": 2, "Turkey": 1, "Sardines": 1},
               (5, 2020): {"Whitefish": 5, "Sardines": 3, "Chicken": 7, "Beef": 3},
               (8, 2020): {"Oceanfish": 3, "Tuna": 2, "Whitefish": 2, "Salmon": 2, "Chicken": 4, "Beef": 2, "Turkey": 1},
               (10, 2020): {"Tuna": 2, "Whitefish": 2, "Salmon": 2, "Chicken": 4, "Beef": 2, "Turkey": 4, "Sardines": 1},
               (12, 2020): {"Chicken": 7, "Beef": 3, "Turkey": 4, "Whitefish": 1, "Sardines": 2},
               (4, 2021): {"Salmon": 2, "Whitefish": 4, "Turkey": 2, "Beef": 4, "Tuna": 3, "MixedGrill": 2},
               (5, 2021): {"Tuna": 5, "Beef": 4, "Scallop": 4, "Chicken": 3},
               (6, 2021): {"Turkey": 2, "Salmon": 2, "Scallop": 5, "Oceanfish": 5, "Sardines": 3},
               (9, 2021): {"Chicken": 8, "Beef": 6},
               (10, 2021): {"Sardines": 1, "Tuna": 2, "Whitefish": 2, "Salmon": 2, "Chicken": 4, "Beef": 2, "Turkey": 4}}

p1a_output = {2019: {'Oceanfish': 13, 'Tuna': 6, 'Whitefish': 7, 'Chicken': 15, 'Beef': 4, 'Salmon': 5, 'Turkey': 1, 'Sardines': 1},
              2020: {'Whitefish': 10, 'Sardines': 6, 'Chicken': 22, 'Beef': 10, 'Oceanfish': 3, 'Tuna': 4, 'Salmon': 4, 'Turkey': 9},
              2021: {'Salmon': 6, 'Whitefish': 6, 'Turkey': 8, 'Beef': 16, 'Tuna': 10, 'MixedGrill': 2, 'Scallop': 9, 'Chicken': 15, 'Oceanfish': 5, 'Sardines': 4}}


# problem 1(a) merge_by_year - 10%


def merge_by_year(feeding_log):
    rDict = {}

    for key, value in feeding_log.items():
        if key[1] not in rDict.keys():
            rDict[key[1]] = {}
        for key1, value1 in value.items():
            if key1 in rDict[key[1]].keys():
                rDict[key[1]][key1] += value1
            else:
                rDict[key[1]][key1] = value1
    return rDict


# print('1a: ', merge_by_year(my_cats_log))
# problem 1(b) merge_year - 15%


def merge_year(feeding_log, year):
    sum = {}

    def helper2(element2, sum):
        if element2[0] in sum.keys():
            sum[element2[0]] += element2[1]
        else:
            sum[element2[0]] = element2[1]

    def helper1(element1, sum):
        list(map(lambda x: helper2(x, sum), element1.items()))

    dateList = list(filter(lambda x: x[0][1] == year, feeding_log.items()))
    list(map(lambda x: helper1(x[1], sum), dateList))
    return sum


# print(merge_year(my_cats_log, 2021))

# problem 1(c) getmax_of_flavor - 15%


def getmax_of_flavor(feeding_log, flavor):
    global max
    max = ((0, 0), 0)

    def helper(date, element):
        global max
        if element[0] == flavor and element[1] > max[1]:
            max = (date, element[1])

    list(map(lambda x: list(map(lambda y: helper(
        x[0], y), x[1].items())), feeding_log.items()))
    return max


graph = {'A': {'B', 'C', 'D'}, 'B': {'C'}, 'C': {'B', 'E', 'F', 'G'}, 'D': {
    'A', 'E', 'F'}, 'E': {'F'}, 'F': {'E', 'G'}, 'G': {}, 'H': {'F', 'G'}}

# problem 2(a) follow_the_follower - 10%


def follow_the_follower(graph):
    rVals = []
    for element in graph.items():
        for element2 in element[1]:
            if element[0] in graph[element2]:
                rVals += [(element[0], element2)]
    return rVals

# problem 2(b) follow_the_follower2 - 6%


def follow_the_follower2(graph):
    rVals = []
    for element in graph.items():
        l = [x for x in element[1] if element[0] in graph[x]]
        if len(l) > 0:
            rVals += [(element[0], l[0])]
    return rVals

# problem 3 - connected - 15%


def connected(graph, node1, node2):
    def rSearch(name, ittr):
        sos = False
        if name == node2:
            return True
        if node2 in graph[name]:
            return True
        if ittr > len(graph):
            return False
        for element in graph[name]:
            if rSearch(element, ittr+1):
                return True
        return False
    return rSearch(node1, 0)

# problem 4(a) - lazy_word_reader - 20%


class lazy_word_reader:

    def __init__(self, name):

        self.file = open(name)
        self.line = []

    def __iter__(self):
        return self

    def __next__(self):

        if not self.line:

            while True:
                temp = self.file.readline()
                if not temp:
                    raise StopIteration
                self.line = temp.split()
                if self.line != []:
                    break

        if len(self.line) != 0:
            return self.line.pop(0)
