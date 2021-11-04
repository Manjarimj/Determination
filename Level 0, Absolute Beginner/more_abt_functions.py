# call by value
def update(b):
    print(id(b))
    b = 21
    print(id(b))
    print(b)


a = 14
print(id(a))
update(a)
a = 13
print(id(a))
print(a)


# call by reference
def update_list(lst):
    lst[0] = 23
    print(*lst)


g_lst = [2, 3, 5, 12, 13, 13]
update_list(g_lst)
print(*g_lst)


