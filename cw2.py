number = int(input("please enter your number :"))


def number_info(n):
    # number = int(input("please enter your number :"))
    if number < 0:
        print("number should be postive")

    elif number == 0:
        raise ValueError
    if n == 1 :
        print(n)

    else:
        number_info(n-1)

    odd = lambda x: x*2
    even = lambda x: x**2
    if n % 2 != 0:
        res = odd(n)
        print(res)
    elif n % 2 == 0:
        res = even(n)
        print(res)




    
number_info(number)