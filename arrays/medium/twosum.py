def twosumByBruteForce(arr,target):

    for i in range(len(arr)):

        for j in range(i+1,len(arr)):

            if(arr[i]+arr[j]==target):
                return True
    return False

def twosumbyMap(arr,target):

    map = {}
    for i in range(len(arr)):

        if target-arr[i] in map:
            return [i,map[target-arr[i]]]
        
        map[arr[i]] = i
        

    return [-1,-1]

arr = list(map(int,input().split()))
res = twosumbyMap(arr,8)
print(res)

