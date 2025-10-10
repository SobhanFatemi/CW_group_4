from datetime import datetime
currect_time = datetime.now().hour
# print(currect_time)
def timer_decorator(start, end):
    def decorator(func):
        def wrapper(*args, **kwargs):

            try:
                 start <= currect_time < end
                 print("ok")
                 return func(*args, **kwargs)
            except ValueError:
                    print("valueerror")
                    return None

        return wrapper
    return decorator




@timer_decorator(start = 7, end = 9)
def work():
    return work


work()
    
