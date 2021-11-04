def func(args1, args2):  # formal args
    return None


func(None, None)  # actual args

"""
types of args
1. Positional Args
2. KeyWord Args
3. Default Args
4. Variable Length
    i) **args
    ii) **kwargs
"""


# position args
def temp(pos1, pos2, pos3):
    return pos1 + pos2 + pos3


print(temp("pos2 ", "pos1 ", "pos3 "))


# keyword args
def temp(pos1, pos2, pos3):
    return pos1 + pos2 + pos3


print(temp(pos2="pos2 ", pos1="pos1 ", pos3="pos3 "))


# default args

def account(name, number, age="18", sex="prefer not to say"):
    w = name + " " + age + " " + sex + " " + number
    print("Account Created for ", w)


account(name="Mullai", age="20.8", number="7010139747")
account(name="someone", age="20.2", sex="male", number="345678")


# variable length args
# I)

def sum(a, b, *c):
    print(a)
    print(b)
    print(c)
    temp = a + b
    for i in c:
        temp += i
    return temp


print(sum(10, 10, 20, 34, 354, 23, 345))


def sum(*a):
    counter = 0
    for i in a:
        counter += i
    return counter


print(sum(2, 2, 2, 2, 2, 2))


# II) **kwargs - key worded variable length args

def account(**arg1):
    print(arg1)


account(name="someone",
        age="20.2",
        sex="male",
        number="345678",
        address="something")