# function for nth fibonacci number
def fibonacci_number(n):
    """
    :param n:
    :return:
    """
    if n <= 0:
        print("Incorrect input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)


print(fibonacci_number(20))


