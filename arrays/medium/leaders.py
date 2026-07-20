def leaders(arr):
    res = []
    for i in range(len(arr)-1):

        if(arr[i] > arr[i+1] and arr[i+1]!=0):
            res.append(arr[i])
        
    res.append(arr[-1])


    return res


arr =  [4, 7, 1, 0]  
res = leaders(arr)
print(res)




