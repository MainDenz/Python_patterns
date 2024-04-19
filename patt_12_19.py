# 1****
# 22***
# 333**
# 4444*
# 55555
print("\nPattern 12")
for i in range(1,6):
    for t in range(1,i+1):
        print(i,end="")
    for y in range(4,i-1,-1):
        print("*",end="")
    print()
print("two")
for i in range(1,6):
    for t in range(1,6):
        if t>i:
            print("*",end="")
        else:
            print(i,end="")
    print()



# 1****
# 12***
# 123**
# 1234*
# 12345
print("\nPattern 13")
for i in range(1,6):
    for t in range(1,i+1):
        print(t,end="")
    for y in range(4,i-1,-1):
        print("*",end="")
    print()
print("Two")
for i in range(1,6):
    for r in range(1,6):
        if i>=r:
            print(r,end="")
        else:
            print("*",end="")
    print()


# 55555
# 4444*
# 333**
# 22***
# 1****
print("\nPattern 14")
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    for l in range(1,6-i):
        print("*",end="")
    print() 
print("Two")
for i in range(5,0,-1):
    for t in range(1,6):
        if t>i:
            print("*",end="")
        else:
            print(i,end="")
    print()




# 12345
# 1234*
# 123**
# 12***
# 1****
print("\nPattern 15")
for i in range(1,6):
    for w in range(1,7-i):
        print(w,end="")
    for r in range(1,i):
        print("*",end="")
    print()
print("Two")
for i in range(5,0,-1):
    for j in range(1,6):
        if j>i:
            print("*",end="")
        else:
            print(j,end="")
    print()




# ****1
# ***22
# **333
# *4444
# 55555

print("\nPattern 16")
for i in range(1,6):
    for t in range(4,i-1,-1):
        print("*",end="")
    for y in range(1,i+1):
        print(i,end="")
    print()
print("Two")
for i in range(1,6):
    for j in range(5,0,-1):
        if j>i:
            print("*",end="")
        else:
            print(i,end="")
    print()



# ****1
# ***21
# **321
# *4321
# 54321

print("\nPattern 17")
for i in range(1,6):
    for j in range(5 , 0, -1):
        if j > i:
            print("*", end="")
        else:
            print(j, end="")
    print()

# 55555
# *4444
# **333
# ***22
# ****1

print("\nPattern 18")
for i in range(5,0,-1):
    for j in range(5,0,-1):
        if j>i:
            print("*",end="")
        else:
            print(i,end="")
    print()

# 54321
# *4321
# **321
# ***21
# ****1

print("\nPattern 19")
for i in range(5,0,-1):
    for j in range(5,0,-1):
        if j>i:
            print("*",end="")
        else:
            print(j,end="")
    print()
