def factorial(n):
    """
    :param n:
    :return:
    """
    if n == 1:
        f = 1
    else:
        f = n * factorial(n - 1)
    return f


if __name__ == '__main__':
    num = int(input("Enter an integer: "))
    result = factorial(num)
    print("the factorial of", num, " is:", result)
