from typing import TypeVar, Callable, List
from algebra.recursion import power

T = TypeVar("T")


#Time Complexity: O(2^n) 
def fibonacci(n: int) -> int:

    assert n >= 1
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

#Time Complexity: O(log n)
def fibonacci_as_matrix(n: int) -> int:

    def matrix_mul(a, b):
        return [
            [
                a[0][0] * b[0][0] + a[0][1] * b[1][0],
                a[0][0] * b[0][1] + a[0][1] * b[1][1],
            ],
            [
                a[1][0] * b[0][0] + a[1][1] * b[1][0],
                a[1][0] * b[0][1] + a[1][1] * b[1][1],
            ],
        ]

    def power(A, n):
        if n == 1:
            return A
        if n % 2 == 0:
            half = power(A, n // 2)  # if it is even then A^n/2*A^n/2

            return matrix_mul(half, half)
        # if it is odd then A*A^n-1
        return matrix_mul(A, power(A, n - 1))

    if n == 0:
        return 0
    base = [[1, 1], [1, 0]]
    result = power(base, n)
    return result[0][1]
