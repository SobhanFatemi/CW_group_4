prices = {"Apple": 60, "Banana": 20, "Orange": 45, "Grapes": 80}

new_dictionary = {key: value for key, value in prices.items() if value > 50}

new_dictionary2 = {key: value*0.9 for key, value in new_dictionary.items() if value > 50}

print(new_dictionary2)
