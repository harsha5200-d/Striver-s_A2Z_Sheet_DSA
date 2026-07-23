def subcount(arr,k):

    presum =0 

    presummap = {}
    count = 0
    presummap[0]=1


    for i in arr:

        presum+=i

        if presum- k in presummap:
            count += presummap[presum-k]

        presummap[presum] = presummap.get(presum,0)+1

    return count 


arr = [3, 1, 2, 4]

resv= subcount(arr,6)
print(resv)
        



        

        