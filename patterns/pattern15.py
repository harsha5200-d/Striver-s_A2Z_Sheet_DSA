def pattern13(n):
    
    for i in range(n,-1,-1):

        for j in range(i):

            print(chr(65+j),end=" ")
            
        
        print()

pattern13(5)