def rotatekleftplaces(arr,k):

    len = len(arr)%k

    for i in range(len):
        popped = arr.pop(0)
        arr.append(popped)

    return arr

arr = list(map(int,input().split()))
res = rotatekleftplaces(arr,3)
print(res)