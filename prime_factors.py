from typing import TypeVar, Callable, List
import math

def smallest_factor(n: int, start: int, stop: int) -> int:
    """Return the smallest factor of n which is >= start and < stop.
    If no such factor exists, then return n.
    If stop < start, then return n."""
    assert n > 1
    assert start > 1
    assert start <= n
   
    for i in range(start, stop, 1):
        if n % i == 0:
            return i
    return n


def prime_factors(n: int) -> List[int]:
    """Returns the list of prime factors of the given integer,
    in increasing order.  If a factor occurs multiple times, it is included
    that many times in the result, so that the product of the factors
    is the given numbers.   The list of factors of 12 is [2, 2, 3].
    Note that the list of prime factors of 1 is [].
    This function should never be called with n=0, as it is impossible to
    return a list of prime numbers whose product is 0."""
    from math import sqrt, ceil

    assert n > 0

    def loop(start, n):
        if n == 1:
            return []
        
        p = smallest_factor(n, start, ceil(sqrt(n)) + 1)
        if p == n:
            return [p]
            raise NotImplementedError()

        else:
            return [p] + loop(p, n // p)
        
    return loop(2, n)


print(prime_factors(16))
