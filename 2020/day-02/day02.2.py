with open("input") as input:
    lines = input.read().splitlines()

correctPasswords = 0

def validate(line):
    minmax=line[0].split('-')
    letter=line[1].strip(':')
    password=line[2]
    minX=int(minmax[0])-1
    maxX=int(minmax[1])-1
    
    p1 = password[minX]
    p2 = password[maxX]
    # print(minX)
    # print(maxX)
    print(p1)
    print(p2)
    print(letter)

    if(bool(p1==letter) ^ bool(p2==letter)):
        return(True)
    else:
        print("this password is invalid")
        print(line)
        print("the letter %s appears in both the %s and the %s locations." %(letter, minX+1, maxX+1))
        return(False)

for line in lines:
    if(validate(line.split())):
        correctPasswords += 1     

print(correctPasswords)

