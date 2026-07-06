def pattern13(n):
    
    for i in range(n-1,-1,-1):

        for j in range(n-(n-i)+1,n+1):

            print(chr(64+j),end=" ")
            
        
        print()

pattern13(5)