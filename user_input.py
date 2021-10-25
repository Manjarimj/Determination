
# string
n = input()
print(n)

# int 
n = int(input()) 
n += 5
print(n)

# space separated Values Ex: length: 5, 1 2 3 4 5
"""
input
5
34 12 54 13 7
"""
l = int(input())
lst = []
for i in range(l):
    temp = int(input())
    lst.append(temp)
print(lst)


lst = list(map(int, input().split()))
print(lst)


