n = eval(input("enter any number --- >  "))

for r in range(n,0,-1):
    for i in range(n,r,-1):
        print(" ",end=" ")
    print("* "* r)

