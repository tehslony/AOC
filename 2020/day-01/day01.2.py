with open("input") as input:
    lines = input.read().splitlines()

numbers=[int(i) for i in lines]
for a in numbers:
    for b in numbers:
        for c in numbers:
            sum = a+b+c
            if(sum==2020):
                product = a*b*c
                print("The three numbers are %d, %d and %d and their product is %d " %(a, b, c, product))