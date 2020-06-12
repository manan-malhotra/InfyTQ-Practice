
#! First sort by number then Name

from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def comprator(a, b):
        if a.score == b.score:
            if a.name > b.name:
                return 1
            else:
                return -1
        return b.score-a.score


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    player = Player(name, score)
    data.append(player)

data = sorted(data, key=cmp_to_key(Player.comprator))
for i in data:
    print(i.name, i.score)
"""
ip->
5
amy 100
dav 100
her 50
aak 75
ale 150

op->
ale 150
amy 100
dav 100
aak 75
her 50
"""
