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
print("\Pattern 54")
for i in range(1,6):
    for j in range(1,6):
        if(j<i):
            print(" ",end="")
        elif(j%2==1):
            print("#",end="")
        else:
            print("*",end="")
    print()




