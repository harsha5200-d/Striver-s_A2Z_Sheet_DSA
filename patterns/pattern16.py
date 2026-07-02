def pattern13(n):
    
    for i in range(n+1):

        for j in range(i):

            print(chr(64+i),end=" ")
            
        
        print()

pattern13(5)