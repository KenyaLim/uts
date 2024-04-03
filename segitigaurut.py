def anu(x):
    x=0
    for i in range(1, x+1):
        for j in range(1, i+1):
            x=x+1
        print(x," ",end="")
    print()

anu(6)