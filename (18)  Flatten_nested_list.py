# Input: [[1,2],[3,4],5] — Output: [1,2,3,4,5]

def flattend_list(nums):
    result =[]
    
    for item in nums:
        if isinstance(item,list):
            for  num in item:
                
                result.append(num)
            
        else:
            result.append(item)
                
                
    return result
print(flattend_list( [[1,2],[3,4],5]))
                
