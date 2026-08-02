def ArmStrong(num):

    # Initialize sum to store the sum of powers of digits
    sum = 0
    temp = num
    # Find the number of digits
    k = len(str(num))

    # Extract digits and add their k-th power to sum
    while temp > 0:

        digit = temp%10
        sum += digit**k
        temp //= 10 
    
    # Check if sum is equal to the original number
    if sum==num:
        return True
    
    return False


res = ArmStrong(370)
print(res)