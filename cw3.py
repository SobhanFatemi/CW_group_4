from datetime import datetime
import functools
currect_time = datetime.now()
def timer_decorator(start, end):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            try:
                 if start <= currect_time < end:
                    print("ok")
                    return func(*args, **kwargs)
                 else:
                     raise ValueError
            except ValueError:
                    print("valueerror")
                    return None

        return wrapper
    return decorator




@timer_decorator(start = 7, end = 9)
def work():
    return work


work()
    
