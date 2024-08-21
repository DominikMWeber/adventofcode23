import re
text = "1this is a 134 test15"
d = dict((m.span(), int(m.group())) for m in re.finditer(r'\d+', text))
print(d)

# TODO: Research about regular expressions to understand them.

data_of_parts = list()

sum = 0

with open("03/sample.txt", "r") as document:

    lines = document.readlines() # Read all lines from document at once.

    for line_iter in range(len(lines)):

        data_of_parts = dict((m.span() , int(m.group())) for m in re.finditer(r'\d+', lines[line_iter]))

        if line_iter == 0:
            # Special case for first line. 
            pass
        elif line_iter == len(lines) - 1:
            # Special case for last line.
            pass
        else:
            # Normal case: Check for any symbols in this line.
            
            idx_char = 0

            for char in lines[line_iter]:

                if not(char.isdigit()) and not ".":

                    # Character is symbol: Use index for finding adjacent numbers.
                    idx_adj = (max(0, idx_char-1), idx_char, min(idx_char+1, len(lines[line_iter])-1))

                    # Check in string above.
                    for key_tuple in data_of_parts:
                        print(key_tuple)

                        if any()

                        continue # Check for next number in this line.


                    # Check in current string.

                    # Check in string beneath.

                    idx_char += 1

                     


