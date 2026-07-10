def sort012(arr):

    low = 0
    high=len(arr)-1
    curr = 0

    while curr < high:

        if arr[curr] == 0:
            arr[curr],arr[low] = arr[low],arr[curr]
            curr+=1
            low+=1

        elif(arr[curr]==1):
            curr+=1
        else:
            arr[curr],arr[high] = arr[high],arr[curr]
            high-=1

    return arr

arr = [1,2,0,2,1,0,1,1,0,0]
res = sort012(arr)
print(res)