from datetime import datetime
<<<<<<< HEAD
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
=======
import random

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            current = datetime.now()
            print(current)
            return func(*args, **kwargs)
        except:
            print("An error happened!")
            return None
    return wrapper
>>>>>>> 2e32c8eb8ae9d1ad75c99b1022e2860a2459995b

@timer_decorator
def simulate_weather(days, start_temp = 25):
    try:
        if days <= 0:
            print("Positive numbers only!")
            return None
        temps = []
        for day in range(days):
            diff = random.randint(-2, 3)
            temps.append(start_temp + diff)
        
        return temps
    except TypeError:
        print("Please enter a number!")
        return None

temps = simulate_weather(10)

max_temp = max(temps)
min_temp = min(temps)
avg_temp = sum(temps)/len(temps)

print(f"Maximum temp: {max_temp}")
print(f"Minimum temp: {min_temp}")
print(f"Average temp: {avg_temp}")