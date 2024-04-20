# A****
# BB***
# CCC**
# DDDD*
# EEEEE
print("Pattern 20")
n=5
for i in range(n):
    for j in range(n):
        if j > i:
            print("*", end="")
        else:
            print(chr(i + 65), end="")
    print()

# A****
# AB***
# ABC**
# ABCD*
# ABCDE
print("Pattern 21")
for i in range(n):
    for j in range(n):
        if j>i:
            print("*",end="")
        else:
            print(chr(j+65),end="")
    print()

# EEEEE
# DDDD*
# CCC**
# BB***
# A****
print("\nPattern 22")
for i in range(4,-1,-1):
    for j in range(5):
        if j>i:
            print("*",end="")
        else:
            print(chr(i+65),end="")
    print()

# ABCDE
# ABCD*
# ABC**
# AB***
# A****
print("\nPattern 23")
for i in range(4,-1,-1):
    for j in range(5):
        if j>i:
            print("*",end="")
        else:
            print(chr(j+65),end="")
    print()
#Note-Inner Loop: The inner loop runs from 0 to 4 (inclusive) with range(5). This loop controls the columns of the pattern.


# ****A
# ***BB
# **CCC
# *DDDD
# EEEEE
print("Pattern 24")
for i in range(n):
    for j in range(4,-1,-1):
        if j > i:
            print("*",end="")
        else:
            print(chr(i+65),end="")
    print()




