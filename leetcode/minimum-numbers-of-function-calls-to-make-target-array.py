class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        allnodes = set(range(n))
        indegree = set(j for i,j in edges)
        return list(allnodes - indegree)