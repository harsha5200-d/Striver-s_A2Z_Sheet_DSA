import math


def divisiors(num):
    res = []
    # Loop from 1 to the square root of the number
    for i in range(1,int(math.sqrt(num))+1):

        # If i is a divisor
        if(num%i==0):
            res.append(i)

            # Check for the paired divisor
            if (i != num//i):
                res.append(num//i)
        
    # Return the divisors in sorted order
    return sorted(res)

resu = divisiors(36)
print(resu)
            

