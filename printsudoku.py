from sudokusolver import *

def print_table(table):
    pieces_of_3 = [' ' + ' '.join(table[i*3: i*3 + 3]) + ' '
                  for i in range(27)]
    row_strings = ['|'.join(pieces_of_3[i*3: i*3 + 3]) for i in range(9)]
    line = ' ' + '+'.join(['-' * 6, '-' * 7, '-' * 6] )
    for n in range(9):
        print(' ' * 10 + row_strings[n])
        if n in [2, 5]: print(' ' * 10 + line)

if __name__ == "__main__":
    print("This script prints a sudoku table when given in a specific format")
    print("")
    print("Example:")
    print("")
    print("Let the string")

    table = '85...24..72......9..4.........1.7..23.5...9...4...........8..7..17..........36.4.'

    print(table)
    print("present the sudoku table. Then the function print_table() will print it as follows:")
    print("")

    print_table(table)

    print("")
    print("More over, using the module sudokusolver, we can solve it. The solution is:")
    print("(Wait for a while)")
    print("")

    solution = solve(table)
    print_table(solution)
    print("")
