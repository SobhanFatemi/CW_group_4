from datetime import datetime
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