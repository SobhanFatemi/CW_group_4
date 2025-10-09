user_input = input("Please enter bunch of names seperated by ',': ")

names = user_input.split(',')

print(names)

names_processed = [name for name in names if len(name) > 3 and name[0] == 'a' or name[0] == 'A']