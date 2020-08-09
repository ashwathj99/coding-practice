def happyLadybugs(b):
    if b.count("_")==len(b): return "YES"
    d = {char:b.count(char) for char in set(b)}
    for col in d:
        if d[col]==1 and col!="_": return "NO"
    try:
        if d["_"]>0: return "YES"
    except:
        i = 0
    if b[1]!=b[0] or b[len(b)-2]!=b[len(b)-1]: return "NO"
    for i in range(1,len(b)-1):
        if b[i]==b[i-1] or b[i]==b[i+1]:
            continue
        else:
            return "NO"
    return "YES"
