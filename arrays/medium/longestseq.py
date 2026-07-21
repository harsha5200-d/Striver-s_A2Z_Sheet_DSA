def longseq(arr):

    if not arr:
        return 0

    ret = sorted(arr)
    count= 0 
    maxi = 0
    for i in range(len(ret)):
        count = 0 
        for j in range(i,len(ret)-1):

            if(ret[j]+1 == ret[j+1]):
                count+=1
                maxi = max(count,maxi)

            elif(ret[j]==ret[j+1]):
                pass

            else:
                break

    return maxi+1


res = longseq([1,6,7,8,9,2,78,90,91,92,93,94,95,96,97])
print(res)



