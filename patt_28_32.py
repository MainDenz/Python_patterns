
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
n=0
for i in range(1,6):
    for j in range(1,6):
        if (j%2==i%2):
            print("*",end=" ")
            n+=1   
        else:
            print(n,end=" ")
    print()





