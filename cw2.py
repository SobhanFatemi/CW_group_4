number = int(input("please enter your number :"))


def number_info(n): 
    # number = int(input("please enter your number :"))
    if number < 0:
        print("number should be postive")

    elif number == 0:
        raise ValueError
    if n == 1 :
        print(1) 
    
    else:
        print(n)
        number_info(n-1)

    
number_info(number)