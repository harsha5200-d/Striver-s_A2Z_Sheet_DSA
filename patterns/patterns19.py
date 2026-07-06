def patterns19(n):

    for i in range(n):

        for j in range(n-i):
            print("*",end="")
        
        for j in range((n-(n-i))*2):
            print(" ",end="")

        for j in range(n-i):
            print("*",end="")
        
        print()

    
    for i in range(n-1,-1,-1):

        for j in range(n-i):
            print("*",end="")
        
        for j in range((n-(n-i))*2):
            print(" ",end="")

        for j in range(n-i):
            print("*",end="")
        
        print()
    


patterns19(5)