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

#         *
#       * *
#     *   *
#   *     *
# * * * * *

print("\n Pattern 75")
for i in range(1,6):
    for j in range(1,6):
        if(j==5 or i+j==6 or i==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#     *
#    * *
#   *   *
#  *     *
# *       *

print("\nPattern 76")
for i in range(5,0,-1):
    for j in range(1,11):
        if(i==j or i+j==10):
            print("*",end="")
        else:
            print(" ",end="")
    print()

# * * * * *
#   *     *
#     *   *
#       * *
#         *

print("\nPattern 77")
for i in range(1,6):
    for j in range(1,6):
        if(i==1 or i==j or j==5):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# *       *
#  *     *
#   *   *
#    * *
#     *

print("\nPattern 78")
for i in range(1,6):
    for j in range(1,10):
        if(i==j or i+j==10):
            print("*",end="")
        else:
            print(" ",end="")
    print()


# *
#  *
#   *
#    *
#   *
#  *
# *
print("\nPattern 79")
for i in range(1,8):
    for j in range(1,5):
        if(j==i or j+i==8):
            print("*",end="")
        else:
            print(" ",end="")
    print()
