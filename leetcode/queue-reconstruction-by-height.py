class Solution:
    def reconstructQueue(self, people):
        n = len(people)
        people.sort(key = lambda x : x[0])
        res = [[-1,-1]]*n
        for i in range(n):
            person = people[i]
            count = person[1]
            for j in range(n):
                if res[j][0]==-1 and count==0:
                    res[j] = person
                    # print(i, res)
                    break
                if res[j][0]==-1 or res[j][0]>=person[0]:
                    count-=1
        return res
"""
Alternate //stefan pochmann
def reconstructQueue(self, people):
    people.sort(key=lambda x: [-x[0], x[1]])
    queue = []
    for p in people:
        queue.insert(p[1], p)
    return queue
"""