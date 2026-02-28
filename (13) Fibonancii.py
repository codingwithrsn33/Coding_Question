#fibonancii

def fibonancii(n):
    first = 0
    second = 1
    
    for i in range(n):
        print (first , end = " ")
        
        next = first + second
        first = second
        second = next
        
(fibonancii(10))
    
    
