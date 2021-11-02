# for loop
for heat in range(10):
    print("temp check", heat)


# for loop

alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(alphabet)):
    print(alphabet[i])

# enhanced for loop (or) for each loop

alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(i)


# while loop

heat = 0
while heat == 12:
    heat += 4
    print("the next person")

print(heat)
print("person with heat 12 is found")


# recursion


def rec(number):
    print("hello", number)
    # to break the recursion
    if number == 0:
        return None
    number -= 1
    rec(number)


rec(12)
# to extend the recursion limit

import sys

sys.setrecursionlimit(100)

def rec(number):
    print("hello", number)
    number -= 1
    rec(number)


rec(0)

# loops with Dictionary

"""
Counter


given = manjari
op = {m : 1, a : 2, n : 1, j : 1, r : 1, i : 1}
given = aabcdggg
op = {a : 2, b : 1, c : 1, d : 1, g : 3}
"""

alphabet = "axdaftyuaikjdrtyujtrseustdjfyuygiuhgff"
d = {}
for i in alphabet:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)