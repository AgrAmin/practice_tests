# Montecarlo and random walk
import random

def random_walk (n):
    x,y = 0,0
    for i in range (n):
        (dx,dy)=random.choice([(0,1),(1,0),(-1,0),(0,-1)])
        x+=dx
        y+=dy
    return (x,y)

number_of_walks = 10000
MinDis=4

for walk_length in range(1,31):
    no_transport = 0
    for i in range (number_of_walks):
        walk=random_walk(25)
        distnace = abs(walk[0])+abs(walk[1])
        if distnace <= MinDis:
            no_transport+=1
    no_transport_percentage = float(no_transport)/number_of_walks
    print('walk size = ', walk_length,
          '/ % of no transport = ',100*no_transport_percentage)
