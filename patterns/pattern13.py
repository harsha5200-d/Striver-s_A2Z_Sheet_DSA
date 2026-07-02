def pattern13(n):
    c=1
    for i in range(n+1):

        for j in range(i):

            print(c,end=" ")
            c+=1
        
        print()

pattern13(5)