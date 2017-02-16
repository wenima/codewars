from itertools import islice

def find_sum(m):
    row = 0
    col = 0
    total = m[row][col]
    end_pos = (len(m) - 1, len(m[0]) - 1)
    while True:
        down = sum([r[col] for r in islice(m, row + 1, None)])
        right = sum(islice(m[row], col + 1, None))
        if down > right:
            row += 1
        else:
            col += 1
        total += m[row][col]
        if (row, col) == end_pos:
            break
    return total
