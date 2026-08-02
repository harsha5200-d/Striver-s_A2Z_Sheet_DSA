import math

# Take integer input from the user
num = int(input())

# Calculate the number of digits using base-10 logarithm
print(int(math.log10(num))+1)