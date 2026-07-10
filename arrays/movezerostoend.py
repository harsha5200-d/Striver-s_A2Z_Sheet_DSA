def movezerosend(arr):

    i= 0
    j = len(arr)-1

    while(i<=j):

        if(arr[i]==0 and arr[j]==0):
            arr[j],arr[i] = arr[i],arr[j]
            j-=1
        elif(arr[i]==0 and arr[j]!=0):
            arr[j],arr[i] = arr[i],arr[j]
            i+=1
            j-=1
        else:
            i+=1

    print(arr)

def movezerosend1(arr):

    j=len(arr)-1

    for i in range(len(arr)):

        if(arr[i]==0):

            arr[i],arr[j] = arr[j],arr[i]
            j-=1
        
    print(arr)

arr = list(map(int,input().split()))
movezerosend(arr)

"""
3 1 2 0 2 0 0 
 3 1 2 0 """
        



        