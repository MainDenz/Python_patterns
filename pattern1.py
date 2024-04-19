
#Notes
# the range() function generates numbers up to, but not including, the specified end value.



#pattern 1
# *****
# *****
# *****
# *****
# *****
print("Pattern 1")
for i in range(1,6):
    for j in range(1,6):
        print("*", end="")
    print()


# *
# **
# ***
# ****
# *****
print("Pattern 2")
for i in range(1,6):
    for j in range(1,i+1):
       print("*", end="")
    print() 


# *****
# ****
# ***
# **
# *
print("Pattern 3")
for i in range(1,6):
    for l in range(5, i-1, -1): # starts from 5 and decrements by 1 each time until it reaches i - 1.
        print("*", end="")
    print()

#     *
#    **
#   ***
#  ****
# *****
print("Pattern 4")
for i in range(1,6):
    for j in range(4,i-1,-1):
        print(" ", end="")
    for m in range(6-i,6):
        print("*", end="")
    print()


# *****
#  ****
#   ***
#    **
#     *
print("Pattern 5")
for i in range(1,6):
    for j in range(6-i,5):
        print(" ", end="")
    for m in range(5,i-1,-1):
        print("*", end="")
    print()


#     *
#    * *
#   * * *
#  * * * *
print("Pattern 6")

for i in range(1,5):
    for j in range(4,i-1,-1):
        print(" ", end="")
    for m in range(1,i+1):
        print("*", end=" ")
    #for l in range(4,i-1,-1):
        #print(" ", end="")
    print()


# * * * * *
#  * * * *
#   * * *
#    * *
#     *
print("Pattern 7")
for i in range(1,6):
    for j in range(1,i):
        print(" ", end="")
    for m in range(5,i-1,-1):
        print("*", end=" ")
    print() 

#     *
#    ***
#   *****
#  *******
# *********
print("Pattern 8")
for i in range(1,6):
    for j in range(4,i-1,-1):
        print(" ", end="")
    for r in range(1,i*2):
        print("*", end="")
    print()

# *********
#  *******
#   *****
#    ***
#     *
print("Pattern 9")
for i in range(1,6):
    for t in range(1,i):
        print(" ", end="")
    for r in range(9,i*2-2,-1):
        print("*", end="")
    print()

# *
# **
# ***
# ****
# ***
# **
# *

print("\nPattern 10")
size = 3
for i in range(size, -size-1, -1):
    for j in range(size, abs(i)-1, -1):
        print("*", end="")
    print()

#    *
#   **
#  ***
# ****
#  ***
#   **
#    *
print("\nPattern 11")
for i in range(3,-4,-1):
    for r in range(1,abs(i)+1):
        print(" ",end="")
    for v in range(3,abs(i)-1,-1):
        print("*",end="")
    print()
