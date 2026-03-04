#  data = [1, 2, 3, 4, 2, 3, 5, 1]
 
def find_duplicates(data):
    duplicates =[]
    
    
    for num in data:
        if data.count(num) > 1 and num not in duplicates:
            duplicates.append(num)
            
    return duplicates
    
print(find_duplicates([1, 2, 3, 4, 2, 3, 5, 1]))
