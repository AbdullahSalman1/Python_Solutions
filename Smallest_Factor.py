from math import sqrt, ceil
from pprint import pprint

def smallest_factor(n, s):
    if n % 2 == 0:  # if n is even
        return 2
    if s % 2 == 0:  # if s is even make it odd bcz we will check only odd
        s += 1

    return next((i for i in range(s, ceil(sqrt(n)) + 1, 2) if n % i == 0), n)


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(f"The smallest factor of {num} is {smallest_factor(num,2)}")
