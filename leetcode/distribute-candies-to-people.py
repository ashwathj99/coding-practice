candies = 60
num_people = 4
distribution = [0]*num_people
i = 0
give = 1
while candies>0:
    if candies<give:
        distribution[i]+=candies
        break
    distribution[i]+=give
    candies = candies - give
    i = (i+1)%num_people
    give = give + 1
print(distribution)