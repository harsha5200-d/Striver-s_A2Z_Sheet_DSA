def pattern10(n):

    for i in range(n):

        for j in range(i):

            print("*",end="")
        
        print()

    

    for i in range(n):

        for j in range(n-i):

            print("*",end="")
        
        print()

pattern10(5)