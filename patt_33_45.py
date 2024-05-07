# 1
# 1* 2
# 1* 2* 3
# 1* 2* 3* 4
# 1* 2* 3* 4* 5
print("Pattern 33")
for i in range(1,6):
    for j in range(1,6):
        if j<i:
            print(j,end="* ")
        elif j==i:
            print(j,end="")
        else:
            break
    print()
'''
#  1
#  3*  2
#  4*  5*  6
# 10* 9* 8*  7
# 11* 12* 13* 14* 15
print("\nPattern 34")
s=1
y=1

for i in range(1,6):
    for j in range(1,i+1):
        if (i%2==1):
            print(s,end=" ")
        else:
            print(y,end=" ")
        s = s+1
    y = y + i - 1
    print()
'''
# #
# **
# ###
# ****
# #####
print("\nPattern 35")
for i in range(1,6):
    for j in range(1,6):
        if (i%2==1 and j<=i):
            print("#",end="")
        elif (i%2==0 and j<=i)  :
            print("*",end="")
        else:
            break
    print()


# 1
# **
# 333
# ****
# 55555
print("\nPattern 36")
for i in range(1,6):
    for j in range(1,6):
        if (i%2==1 and j<=i):
            print(i,end="")
        elif (i%2==0 and j<=i)  :
            print("*",end="")
        else:
            break
    print()

# 1
# **
# 123
# ****
# 12345
print("\nPattern 37")
for i in range(1,6):
    for j in range(1,6):
        if (i%2==1 and j<=i):
            print(j,end="")
        elif (i%2==0 and j<=i)  :
            print("*",end="")
        else:
            break
    print()


# 1
# 1*
# 1*3
# 1*3*
# 1*3*5”

print("\nPattern 38")
for i in range(1,6):
    for j in range(1,6):
        if (j<=i):
            if(j%2==1):
                print(j,end="")
            else:
                print("*",end="")
        else:
            break
    print()

# 1
# 2*
# 3*3
# 4*4*
# 5*5*5”

print("\nPattern 39")
for i in range(1,6):
    for j in range(1,6):
        if (j<=i):
            if(j%2==1):
                print(i,end="")
            else:
                print("*",end="")
        else:
            break
    print()

# #####
# ****
# ###
# **
# #
print("\nPattern 40")
for i in range(6,1,-1):
    for j in range(1,i):
        if(i%2==0):
            print("#",end="")
        else:
            print("*",end="")
    print()


# #*#*#
# #*#*
# #*#
# #*
# #
print("\nPattern 41")
for i in range(6,1,-1):
    for j in range(1,i):
        if(j%2==1):
            print("#",end="")
        else:
            print("*",end="")
    print()

# 55555
# ****
# 333
# **
# 1
print("\nPattern 42")
for i in range(5,0,-1):
    for j in range(1,i+1):
        if(i%2==1):
            print(i,end="")
        else:
            print("*",end="")
    print()

# 12345
# ****
# 123
# **
# 1
print("\nPattern 43")
for i in range(5,0,-1):
    for j in range(1,i+1):
        if(i%2==1):
            print(j,end="")
        else:
            print("*",end="")
    print()


# 1*3*5
# 1*3*
# 1*3
# 1*
# 1”
print("\nPattern 44")
for i in range(6,1,-1):
    for j in range(1,i):
        if (j%2==1):
            print(j,end="")
        else:
            print("*",end="")
    print()

