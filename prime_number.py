# generate prime numbers from 1 to N

def prime_num(n):
    """
    :param :
    :return:
    """
    for n in range(2, num):
        for i in range(2, n):
            if n % i == 0:
                return n
                break
    else:
        print(n)


if __name__ == '__main__':
    number = int(input("Enter the range: "))
    print(prime_num(number))


