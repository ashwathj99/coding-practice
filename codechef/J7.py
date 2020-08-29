def volume(p,s,h):
    val = h*(p/4 - h)
    return (s/2 - val)*h

for _ in range(int(input())):
    p, s = map(int, input().split())
    D = (p**2 - 8*s)
    h1 = (p + D**0.5)/4
    h2 = (p - D**0.5)/4
    print(h1, h2)
    if h2>0:
        v1 = volume(p,s,h1)
        v2 = volume(p,s,h2)
        print(v1,v2)
        continue
    print(volume(p,s,h1))

# print(2**0.5)