user_input = input("Please enter bunch of names seperated by ',': ")

names = user_input.replace(" ", ",")
names_add = names.split(",")

names_processed = [name for name in names_add if len(name) > 3 and name[0] == 'a' or name[0] == 'A']


# ali amir nima
sorted_user = sorted(names_processed)
with open('names.txt', 'w') as file:
    file.write(str(sorted_user))


print(sorted_user)