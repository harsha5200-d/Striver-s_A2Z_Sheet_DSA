def pattern11(n):
    
    
    for i in range(n):

        toggle = 1 if (i%2==0 or i==0) else 0

        for j in range(i+1):

            print(toggle,end=" ")
            toggle = 0 if toggle==1 else 1

        print()

pattern11(10)

            
