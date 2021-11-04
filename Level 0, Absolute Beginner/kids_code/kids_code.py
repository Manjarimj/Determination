"""Palindrome
ex: malayalam, madam"""


def palindrome_or_not(args):
    print(args[::-1])
    return args == args[::-1]


def prime(num):
    for i in range(2, num):
        if num % 2 == 0:
            return False
    return True


def odd_or_even(num):
    return num % 2 == 0


def factorial(num):  # 5
    ans = 1
    for i in range(2, num + 1):
        ans *= i
    return ans


def fibonacci(num):
    a = 0
    b = 1
    for i in range(num - 2):
        print(a)
        c = a + b
        a = b
        b = c


"""
a = 101
b = 234
stdout:
101
111
121
.
.
.
232
"""


def palidromes_at_the_given_range(a, b):
    for i in range(a, b + 1):
        if str(i) == str(i)[::-1]:
            print(i)


def armstrong(num):
    pass


def funnynumber(num):
    pass
