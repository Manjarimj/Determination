"""create an counter for a str givn by the user"""
str = input() # "how was your day"
d = {}
for i in str:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d.items())
# print the elements which are repeating only two times
for i,j in d.items():
    if j == 2:
        print(i)


# how many elements were repeating only two times
count = 0
for j in d.values():
    if j == 2:
        count += 1
print(count)

    

