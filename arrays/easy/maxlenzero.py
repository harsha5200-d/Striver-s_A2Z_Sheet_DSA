def maxcountzero(arr):
    
    max_len = 0
    for i in range(len(arr)):

        curr_sum = 0

        for j in range(i,len(arr)):
            curr_sum += arr[j]

            if curr_sum == 0:
                max_len = max((j-i)+1,max_len)


    return max_len

arr = [1,0,2,2,-1,-1]
res = maxcountzero(arr)
print(res)



        

        


            