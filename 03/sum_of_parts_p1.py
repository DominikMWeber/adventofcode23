"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

To begin, get your puzzle input.
"""

sum = 0

def is_symbol(row, col):

    # Clip rows and col to index range.
    if row >= ctn_rows:
        row = ctn_rows-1
    if row < 0:
        row = 0
    if col >= ctn_columns:
        col = ctn_columns-1
    if col < 0:
        col = 0

    if (not lines[row][col].isdigit()) and \
        (lines[row][col] != ".") and \
            (lines[row][col] != "\n"):
        return True

    return False

def is_valid_number(row, col):
    
    valid = False

    # Check line above.
    if row >= 1: 
        if is_symbol(row-1, col-1) or \
           is_symbol(row-1, col) or \
            is_symbol(row-1, col+1):
            valid = True

    # Check current line.
    if is_symbol(row, col-1) or \
        is_symbol(row, col+1):
        valid = True

    # Check line beneath.
    if row < ctn_rows:
        if is_symbol(row+1, col-1) or \
           is_symbol(row+1, col) or \
            is_symbol(row+1, col+1):
            valid = True

    return valid

with open("03/input.txt", "r") as document:

    lines = document.readlines() 

    num_str = ""
    was_num = False
    num_is_valid = False

    ctn_rows = len(lines)
    ctn_columns = len(lines[0])

    i = 0
    while i < ctn_rows:
        j = 0
        while j < ctn_columns:

            ch = lines[i][j]
            if ch.isdigit():
                was_num = True
                num_str += ch

                # Check if number is not valid
                if is_valid_number(i, j):
                    num_is_valid = True

            elif was_num == True:
                was_num = False

                if num_is_valid == True:
                    sum += int(num_str)
                    
                num_is_valid = False
                num_str = ""
            
            j += 1

        i += 1

print(sum)