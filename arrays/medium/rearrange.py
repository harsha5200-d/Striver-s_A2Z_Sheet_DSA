def rearrange(arr):
    pos = []
    neg = []
    # [1,2,-4,-5]
    for i in range(len(arr)):

        if(arr[i]<0):
            neg.append(arr[i]) #[1,2]
        else:
            pos.append(arr[i])

    for i in range(len(arr)//2): #[-4,-5]

        arr[i*2] = pos[i]    # arr[0] = pos[0] #arr[2] = pos[1]
        arr[(i*2)+1] = neg[i] # arr[1] = pos[0] #arr[3] = neg[1]

    return arr

arr = [1,2,3,-1,-2,-3,1,2,3,-1,-2,-3]
res = rearrange(arr)
print(res)


        