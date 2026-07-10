def twosumByBruteForce(arr,target):

    for i in range(len(arr)):

        for j in range(i+1,len(arr)):

            if(arr[i]+arr[j]==target):
                return True
    return False


arr = list(map(int,input().split()))
res = twosumByBruteForce(arr,70)
print(res)