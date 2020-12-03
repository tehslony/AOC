with open("input") as input:
    lines = input.read().splitlines()

correctPasswords = 0

def validate(line):
    minmax=line[0].split('-')
    letter=line[1].strip(':')
    password=line[2]
    minX=int(minmax[0])
    maxX=int(minmax[1])

    if(minX<=password.count(letter)<=maxX):
        return(True)
    else:
        print("there are %d occurrences of the letter %s in the password %s. There should be between %d and %d occurrences" %(password.count(letter), letter, password, minX, maxX))
        print(line)
        print("this password is invalid")
        return(False)

for line in lines:
    if(validate(line.split())):
        correctPasswords += 1     

print(correctPasswords)

