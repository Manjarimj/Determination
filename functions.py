def userdefined_isupper(a):
    ans = ord(a)
    if 65 <= ans <= 90:
        return True
    else:
        return False


b = "r"
d = "W"
ans = userdefined_isupper(b)
ans1 = userdefined_isupper(d)
print(ans)
print(ans)

