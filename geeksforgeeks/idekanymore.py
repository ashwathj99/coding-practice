#why is this mf matrix not working properly you have one job
t = [[None]*5 for i in range(5)]

for i in range(5):
    for j in range(5):
        if i==0 or j==0:
            t[i][j] = i+j
t[4][4]=20
for row in t:
    print(row)