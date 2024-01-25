sum = 0

with open("input.txt", "r") as document:

    lines = document.readlines()

    for line in lines:
        
        first = True
        digit = 0
        for char in line:

            if str(char).isdigit():

                digit = int(char)

                if first == True:

                    sum += digit * 10
                    first = False
        
        sum += digit

    print(sum)