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

#  1
#  3*  2
#  4*  5*  6
# 10*  9*  8*  7
# 11* 12* 13* 14* 15
print("\nPattern 34")
s=1

'''for i in range(1,6):
    for j in range(1,6):
        if j==1:
            print(s,end="")
            s+=i
        else:
            break
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


