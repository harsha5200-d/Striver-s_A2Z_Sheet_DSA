def print1ton(count,n):

    if(count>=n):
        return 
    
    print(count)

    print1ton(count+1,n)

print1ton(0,100)

    