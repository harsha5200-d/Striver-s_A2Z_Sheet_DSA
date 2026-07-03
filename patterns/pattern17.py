def pattern13(n):
    
    for i in range(n+1):

        for j in range(n-i):
            print(" ",end="")

        for j in range(i):
            print(chr(65+j),end="")

        for j in range(i-1,0,-1):
            print(chr(64+j),end="")
            
        print()

pattern13(4)