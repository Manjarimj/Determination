# List

"""
C++ Array, 
int arr[5] = {2,2,45,4,32}
"""

lst = [1,"string",'q',2.334,999999999999,9.1234565432345678, True]
lst.append(23)
lst.insert(2, "new guy")
print(lst)
lst.pop()
lst.pop(1)
lst.remove('q')
lst = [12,12,434,234,0.234]
print(lst[3])
lst.sort()
lst.reverse()
print(lst.index(434))
print(lst.__contains__(12))
print(len(lst))
print(lst)
lst2 = lst + [123,23,345,456]
print(lst2)

a = "abcdefgh"
lst_str = list(a)
print(lst_str)

# Tuple

tpl = (12,23,23,23,432)
print(tpl.index(12))
print(tpl.count(23))
print(tpl)

# Set

st = {12, 12, 23, 35, 23}
st.remove(12)
st.add(43)
st.pop()
print(st)

# Dictionary

dct = {12 : "2342", 23:'1313', "23":13}
print(dct[12])
print(dct.keys())
print(dct.values())
print(dct.items())
dct[123] = "new"
print(dct)
dct[123] = "old"
print(dct)








