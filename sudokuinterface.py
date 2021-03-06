from sudokusolver import *
from printsudoku import *

print('Give your unsolved sudoku as a 81 character string as follows:')
print('First 9 characters present first row, next 9 second row and so on.')
print('Empty squares are presented as dots.')

table = input('write the string representation here (without quote marks):')

validicity = ['The sudoku is not valid. It dose not have any solutions.',
    'Unique solution found. It is:',
    'The sudoku is not valid. Multiple solutions found.']

def check_validicity(solution):
    if len(solution) < 81: return validicity[0]
    if len(solution) == 81: return validicity[1]
    return validicity[2] 

solution = solve(table)
print(len(solution))
print(solution)
valid = check_validicity(solution)
print(valid)
if valid == validicity[1]:
    print_table(solution)
