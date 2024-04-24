
# 1 2 3 4 *
# 1 2 3 * 5
# 1 2 * 4 5
# 1 * 3 4 5
# * 2 3 4 5
print("Pattern 28")
for i in range(5,0,-1):
    for j in range(1,6):
        if (j==i):
            print("*",end=" ")
        else:
            print(j,end=" ")
    print() 

#  * 1 * 2 *
#  3 * 4 * 5
#  * 6 * 7 *
#  8 * 9 *10
#  *11 *12 *

print("\nPattern 29")
z=0
for i in range(1,6):
    for j in range(1,6):
        if (j%2==i%2):
            print("*",end=" ")
            z+=1   
        else:
            print(z,end=" ")
    print()



# * A* B*
# C* D* E
# * F* G*
# H* I* J
# * K* L*

print("\nPattern 30")
y = ord("A")
for i in range(1,6):
    for j in range(1,6):
        if(j%2==i%2):
            print("*",end=" ")
        else:
            print(chr(y),end=" ")
            y+=1
    print()



#  * # # # # # #
#  # # # # # * *
#  * * * # # # #
#  # # # * * * *
#  * * * # # # #
#  # # # # # * *
#  * # # # # # #

'''print("\nPattern 31")
for i in range(3,-4,-1):
    if(i%2==1):
        for j in range(1,7):
            if(j==1):
                print("#",end=" ")
            elif(j<i):
                print("*",end=" ")

            else:
                print("#",end=" ")
'''
print("\nPattern 31")
n = 7
x = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i % 2 == 1 and j <= x:
            print("* ", end="")
        elif i % 2 == 0 and j >= n - x + 1:
            print("* ", end="")
        else:
            print("# ", end="")
    print()
    if i <= n // 2:
        x += 1
    else:
        x -= 1


#  * 0 0 0 * 0 0 0 *
#  0 * 0 0 * 0 0 * 0
#  0 0 * 0 * 0 * 0 0
#  0 0 0 * * * 0 0 0
#  0 0 0 0 * 0 0 0 0

print("\nPattern 32")
for i in range(1,6):
    for j in range(1,10):
        if (j==i or j==5 or j==10-i):
            print("*",end=" ")
        else:
            print("0",end=" ")
    print()
