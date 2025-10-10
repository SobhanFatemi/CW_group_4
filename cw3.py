from datetime import datetime
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            current = datetime.now()
            print(current)
            result = func(*args, **kwargs)
            return result
        except:
            print("An error happened!")
            return None
    return wrapper

@timer_decorator
def work():
    print("Working...")

work()