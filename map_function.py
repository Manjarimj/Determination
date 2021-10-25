def divide_by(num):
    return int(num/2)


lst = [12, 34, 56, 78, 14]

# without using map function
for i in range(len(lst)):
    lst[i] = divide_by(lst[i])

print(lst)

#using map function
ans = map(divide_by, lst)

for i in ans:
    print(i)




