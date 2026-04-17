def my_decorator(func):
    def wrapper():
        print("Befor Func")
        
        func()
        print("After the func")
    
    return wrapper


@my_decorator
def say_hello():
    print("okay")
    
say_hello()
