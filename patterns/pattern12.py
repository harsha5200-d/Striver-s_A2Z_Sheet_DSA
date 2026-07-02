def pattern12(n):

    
    for i in range(n+1):

        for j in range(1,i+1):
            print(j,end="")
        
        for j in range(((n+1)*2)-(i+1)*2):
            print(" ",end="")
        
        for j in range(i,0,-1):
            print(j,end="")
        
        print()
    
pattern12(5)

