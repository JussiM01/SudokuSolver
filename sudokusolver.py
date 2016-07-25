def solve(table):
    i = table.find('.')
    if i == -1: return table
    return [s for n in range(1, 10) if fits(table, i, str(n))
            for s in solve(table[:i] + str(n) + table[i+1:])]

def fits(table, i, c):
    for j in range(81):
        if table[j] == c and (row_eq(i, j) or col_eq(i, j) or block_eq(i, j)):
            return False
    return True

def row_eq(i, j): return i // 9 == j // 9
def col_eq(i, j): return i % 9 == j % 9
def block_eq(i, j):
    return (i // 9 // 3 == j // 9 // 3) and (i % 9 // 3 == j % 9 // 3)
