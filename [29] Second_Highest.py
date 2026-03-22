def find_lar(arr):
    if len(arr) < 2:
        return False
        
    largest = arr[0]
    second = arr[0]
    
    for num in arr:
        if num > largest:
            largest = second
            largest = num
        elif num > second and num != largest:  
            second = num  
            
    return second
print(find_lar([10,3,4,55,34]))
        
