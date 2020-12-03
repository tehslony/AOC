with open("input") as input:
    lines = input.read().splitlines()

def testNum(i):
    for x in lines:
        x=int(x)
        sum=i+x
        print("%d+%d=%d" %(i, x, sum))
        if sum<2020:
            for z in lines:
                z=int(z)
                threesum=sum+z
                if threesum==2020
                    return(x)

for i in lines:
    i=int(i)
    x = testNum(i)
    if(x):
        print("the two numbers are %d, and %d" %(i, x))
        print("and the product of the two numbers is: %d" %(i*x ))
        break
    
