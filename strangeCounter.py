t = 10**12
if t<4:
    print(4-t)
cycle = 1
prevstarttime = 1
prevendtime = 3
prevstartvalue = 3
currstarttime = 0
while 1:
    cycle+=1
    currstartvalue = prevstartvalue*2
    currstarttime+= prevstartvalue
    if cycle==2:
        currstarttime+=1
    currendtime = prevendtime+currstartvalue
    if t>=currstarttime and t<=currendtime:
        #code
        print(cycle)
        temp = currstarttime+currstartvalue
        # print("currstarttime = ", currstarttime)
        # print("currstartvalue = ", currstartvalue)
        ans = temp - t
        print(ans)
        break
    else:
        prevendtime = currendtime
        prevstartvalue = currstartvalue
        continue