def printNamaNtimes(n,name):

    if(n==0):
        return 
    
    print(name)

    printNamaNtimes(n-1,name)

printNamaNtimes(3,"krishna")