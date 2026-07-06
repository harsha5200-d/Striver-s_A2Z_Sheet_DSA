import math


def divisiors(num):
    res = []
    for i in range(1,int(math.sqrt(num))+1):

        if(num%i==0):
            res.append(i)

            if (i != num//i):
                res.append(num//i)
        
    return sorted(res)

resu = divisiors(36)
print(resu)
            

