Prices = {"Apple": 60, "Banana": 20, "Orange": 45, "Grapes": 80}

new_dictionary = {key : value*0.9 for key , value in Prices.items() if value > 50}
print(new_dictionary)
