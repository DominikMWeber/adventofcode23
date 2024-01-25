import sys

# DIESE LÖSUNG FINDET ZIFFERN NICHT, DIE MEHRFACH IM STRING VORKOMMEN

sum = 0
word_digits = { "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9,
               "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9 }

with open("input.txt", "r") as document:

    lines = document.readlines()

    for line in lines:
        
        digit = 0
        min_index = sys.maxsize
        max_index = -1
        min_digit = 0
        max_digit = 0

        for key in word_digits:

            index = line.find(key)

            if index != -1: # Key was found.
    
                if index <= min_index:
                    min_index = index
                    min_digit = word_digits[key]
                
                if index >= max_index:
                    max_index = index
                    max_digit = word_digits[key]

        # Check for values at min_index and max_index.
        digit = min_digit * 10 + max_digit

        print(digit, min_digit, max_digit)
        sum += digit

    print(sum)