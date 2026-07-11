def buysellstock(arr):

    curr_max = 0
    max_len = 0
    for i in range(len(arr)):

        for j in range(i+1,len(arr)):

            curr_max = arr[j]-arr[i]

            max_len = max(max_len,curr_max)

    return max_len

def byoptimalapproach(arr):

    mini = float('inf')
    curr_max = 0
    for i in range(len(arr)):

        if(arr[i] < mini):
            mini = arr[i]

        curr_max = max(curr_max,arr[i]-mini)
        
    return curr_max
            

arr = [7,1,5,3,6,4]
res = byoptimalapproach(arr)
print(res)
