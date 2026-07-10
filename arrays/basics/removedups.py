def removedups(arr):

    i=0
    for j in range(1,len(arr)):

        if(arr[i]==arr[j]):
            
            i+=1
            arr[i] = arr[j]
        
    return i+1



arr = list(map(int,input().split()))
res = removedups(arr)
print(arr[res])

