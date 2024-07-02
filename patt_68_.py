# *   *
#  * *
#   *
#  * *
# *   *

print("\nPattern 68")
for i in range(1,6):
    for j in range(1,6):
        if (i == j or i + j == 6):
            print("*",end="")
        else:
            print(" ",end="")
    print()

#   *
#   *
# *****
#   *
#   *
print("\nPattern 69")
for i in range(1,6):
    for j in range(1,6):
        if(i==3 or j == 3):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# *****
# *   *
# *   *
# *   *
# *****
print("\nPattern 70")
for i in range(1,6):
    for j in range(1,6):
        if(i == 1 or i == 5):
            print("*",end="")
        elif(j==1 or j==5):
            print("*",end="")
        else:
            print(" ", end="")
    print()

# *****
# *###*
# *###*
# *###*
# *****
print("\nPattern 71")
for i in range(1,6):
    for j in range(1,6):
        if(i == 1 or i == 5):
            print("*",end="")
        elif(j==1 or j==5):
            print("*",end="")
        else:
            print("#", end="")
    print()

# *******
# **   **
# * * * *
# *  *  *
# * * * *
# **   **
# *******

print("\nPattern 72")
for i in range(1,8):
    for j in range(1,8):
        if (i==1 or i==7 or i==j or i+j==8 or j==1 or j==7):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# *
# * *
# *   *
# *     *
# *       *
# *         *
# * * * * * * *
print("\nPattern 73")
for i in range(1,8):
    for j in range(1,8):
        if(i==7 or i==j or j==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# * * * * * * *
# *         *
# *       *
# *     *
# *   *
# * *
# *
print("\nPattern 74")
for i in range(1,8):
    for j in range(1,8):
        if(i==1 or i+j==8 or j==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
