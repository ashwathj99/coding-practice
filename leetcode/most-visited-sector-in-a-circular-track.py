def func(n, rounds):
    vis=[0]*(n+1)
    vis[rounds[0]]=1
    for i in range(1,len(rounds)):
        if(rounds[i-1]<=rounds[i]):
            for j in range(rounds[i-1]+1,rounds[i]+1):
                vis[j]+=1
        else:
            for j in range(rounds[i-1]+1,n+1):
                vis[j]+=1
            for j in range(1,rounds[i]+1):
                vis[j]+=1
    ans=[]
    m=max(vis)
    for i in range(len(vis)):
        if(vis[i]==m):
            ans.append(i)
    print(ans)

n = 4
rounds = [1,3,1,2]
func(n, rounds)