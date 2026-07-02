def pattern7(n):

    for i in range(n):

        for j in range(n-i):
            print(" ",end="")
            
        for j in range((i*2)+1):

            print("*",end="")
            
        print()
        
pattern7(5)