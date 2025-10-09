user_input = input("Please enter bunch of names seperated by ',': ")

names = user_input.replace(" ", ",")
names_add = names.split(",")

names_processed = [name for name in names_add if len(name) > 3 and name[0] == 'a' or name[0] == 'A']


# ali amir nima arman ahmad
sorted_user = sorted(names_processed)

try: 
    with open('names.txt', 'w') as file:
        counter = 0
        for name in sorted_user:
            counter += 1
            file.write(name + '\n')
        file.write(f"Total number of names: {counter}")
    print(f"file saved successfully with {counter} name")
except FileNotFoundError as error :
    print("error")
print(sorted_user)