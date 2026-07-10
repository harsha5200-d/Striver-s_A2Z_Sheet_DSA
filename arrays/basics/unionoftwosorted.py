def UNionOFTwoSortedArrays(arr1,arr2):

    n1 = len(arr1)
    n2 = len(arr2)
    i=0
    j=0
    uni = []
    while i<n1 and j<n2:

        if(arr1[i]<arr2[j]):
            
            if arr1[i] not in uni:
                uni.append(arr1[i])
            i+=1
        
        elif(arr1[i]>arr2[j]):
            if arr2[j] not in uni:
                uni.append(arr2[j])
            j+=1
        
        

    
    while i<n1:
        
        if arr1[i] not in uni:
            uni.append(arr1[i])

        i+=1
    
    while j<n2:
        if arr2[j] not in uni:
            uni.append(arr2[j])
        j+=1


    return uni


arr1 = [3,5,8,9,77,90]
arr2 = [35,89,773,90]

res = UNionOFTwoSortedArrays(arr1,arr2)
print(res)




