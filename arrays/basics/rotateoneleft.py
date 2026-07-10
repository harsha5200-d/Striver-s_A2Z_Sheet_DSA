def rotateleft(arr):

    temp = arr[0]

    for i in range(1,len(arr)):

        arr[i-1] = arr[i]

    arr[-1] = temp

   

arr = list(map(int,input().split()))
rotateleft(arr)
print(arr)