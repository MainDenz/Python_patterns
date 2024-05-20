#     #
#    **
#   ###
#  ****
# #####

print("\nPattern 46")
for i in range(1,6):
    for j in range(5,0,-1):
        if(j>i):
            print(" ",end="")
        elif(i%2==1):
            print("#",end="")
        else:
            print("*",end="")
    print()

#     #
#    *#
#   #*#
#  *#*#
# #*#*#

print("\nPattern 47")
for i in range(1,6):
    for j in range(5,0,-1):
        if(j>i):
            print(" ",end="")
        elif(j%2==1):
            print("#",end="")
        else:
            print("*",end="")
    print()


#     1
#    **
#   333
#  ****
# 55555
print("\nPattern 48")
for i in range(1,6):
    for j in range(5,0,-1):
        if(j>i):
            print(" ",end="")
        elif(i%2==1):
            print(i,end="")
        else:
            print("*",end="")
    print()

#     1
#    **
#   321
#  ****
# 54321
print("\nPattern 49")
for i in range(1,6):
    for j in range(5,0,-1):
        if(j>i):
            print(" ",end="")
        elif(i%2==1):
            print(j,end="")
        else:
            print("*",end="")
    print() 



#     5
#    **
#   345
#  ****
# 12345
print("\nPattern 50")
for i in range(5,0,-1):
    for j in range(1,6):
        if(j<i):
            print(" ",end="")
        elif(i%2==1):
            print(j,end="")
        else:
            print("*",end="")
    print() 



#     1
#    *1
#   3*1
#  *3*1
# 5*3*1”
print("\nPattern 51")
for i in range(1,6):
    for j in range(5,0,-1):
        if(j>i):
            print(" ",end="")
        elif(j%2==0):
            print("*",end="")
        else:
            print(j,end="")
    print()


#     1
#    *2
#   3*3
#  *4*4
# 5*5*5
print("\nPattern 52")
for i in range(1,6):
    for j in range(5,0,-1):
        if(j>i):
            print(" ",end="")
        elif(j%2==1):
            print(i,end="")
        else:
            print("*",end="")
    print()

# #####
#  ****
#   ###
#    **
#     #
print("\nPattern 53")
for i in range(1,6):
    for j in range(1,6):
        if(j<i):
            print(" ",end="")
        elif(i%2==1):
            print("#",end="")
        else:
            print("*",end="")
    print()

# #*#*#
#  *#*#
#   #*#
#    *#
#     #
print("\nPattern 54")
for i in range(1,6):
    for j in range(1,6):
        if(j<i):
            print(" ",end="")
        elif(j%2==1):
            print("#",end="")
        else:
            print("*",end="")
    print()

# 55555
#  ****
#   333
#    **
#     1
print("\nPattern 55")
for i in range(5,0,-1):
    for j in range(5,0,-1):
        if (j>i):
            print(" ",end="")
        elif(i%2==0):
            print("*",end="")
        else:
            print(i,end="")
    print()


# 54321
#  ****
#   321
#    **
#     1
print("\nPattern 56")
for i in range(5,0,-1):
    for j in range(5,0,-1):
        if(j>i):
            print(" ",end="")
        elif(i%2==0):
            print("*",end="")
        else:
            print(j,end="")
    print()



# 5*3*1
#  *3*1
#   3*1
#    *1
#     1
print("\nPattern 57")
for i in range(5,0,-1):
    for j in range(5,0,-1):
        if (j>i):
            print(" ",end="")
        elif(j%2==1):
            print(j,end="")
        else:
            print("*",end="")
    print()


#     #
#    * *
#   # # #
#  * * * *
# # # # # #
print("\nPattern 58")
for i in range(1,6):
    for j in range(5,0,-1):
        if (j>i):
            print(" ",end="")
        elif(i%2==0):
            print("*",end=" ")
        else:
            print("#",end=" ")
    print()


#     #
#    * #
#   # * #
#  * # * #
print("\nPattern 59")
for i in range(1,5):
    for j in range(4,0,-1):
        if(j>i):
            print(" ",end="")
        elif(j%2==0):
            print("*",end=" ")
        else:
            print("#",end=" ")
    print()

#     1
#    * *
#   3 3 3
#  * * * *
# 5 5 5 5 5
print("\nPattern 60")
for i in range(1,6):
    for j in range(5,0,-1):
        if(j>i):
            print(" ",end="")
        elif(i%2==0):
            print("*",end=" ")
        else:
            print(i,end=" ")
    print()
        
print("\n Bonus Pattern")
for i in range(5,0,-1):
    for j in range(1,6):
        if(j>i):
            print(chr(i + 64), end=" ")
        else:
            print(chr(j + 64), end=" ")
    print()



