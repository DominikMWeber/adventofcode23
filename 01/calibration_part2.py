import sys

sum = 0
word_digits = { "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9,
               "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9 }

with open("input.txt", "r") as document:

    lines = document.readlines()

    for line in lines:
        
        found_front = False
        found_back = False
        min_digit = 0
        max_digit = 0
        
        for x in range(1, len(line) + 1):

            front_str = line[0:x]
            back_str = line[-x:]

            for key in word_digits:
                
                index_front = front_str.find(key)
                index_back = back_str.find(key)

                if index_front != -1 and found_front == False:
                    min_digit = word_digits[key]
                    found_front = True

                if index_back != -1 and found_back == False:

                    max_digit = word_digits[key]
                    found_back = True 

        # Check for values at min_index and max_index.
        digit = min_digit * 10 + max_digit

        print(digit, min_digit, max_digit)
        sum += digit

    print(sum)



