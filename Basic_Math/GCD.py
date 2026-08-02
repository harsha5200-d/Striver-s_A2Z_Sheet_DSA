def gcd(n1,n2):

    # Iterate from the minimum of the two numbers down to 1
    for i in range(min(n1,n2),0,-1):

        # Check if i divides both numbers without a remainder
        if(n1%i==0 and n2%i==0):
            return i
        
    return -1

res = gcd(30,15)
print(res)