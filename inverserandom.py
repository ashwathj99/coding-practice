import random
import math
Lambda = 1
for i in range(200):
    rand = random.random()
    x = -math.log(1-rand)
    print("random number: ", rand, "\tx" + str(i) + ':', x)