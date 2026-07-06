def ArmStrong(num):

    sum = 0
    temp = num
    k = len(str(num))

    while temp > 0:

        digit = temp%10
        sum += digit**k
        temp //= 10 
    
    if sum==num:
        return True
    
    return False


res = ArmStrong(370)
print(res)