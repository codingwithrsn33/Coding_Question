def merge_list(list1,list2):
    arr = list1 + list2
    
    for i in range(len(arr)):
        for j in range(i+1 , len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                
    result = []
    
    for num in arr :
        if num not in result:
            result.append(num)
    return result
    
print(merge_list([1,5,3],[8,2,5]))

output = [1, 2, 3, 5, 8]

=== Code Execution Successful ===
