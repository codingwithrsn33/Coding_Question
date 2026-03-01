def two_sum(nums,target):
    seen ={}
    
    for index , num in enumerate(nums):
        need = target - num 
        if need in seen:
            return [seen[need] ,index]
            
        if num not in seen:
            seen[num] = index
            
print(two_sum([2,3,4,5,4,3,3,32,2], 35))
        
        
