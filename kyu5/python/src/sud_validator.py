"""Module to solve the code-kata https://www.codewars.com/kata/did-i-finish-my-sudoku/."""

def done_or_not(board):
    """Return a message to the user if the given Sudoku board is valid or not."""
    for l in board + list(zip(*board)) + [sum((board[x+k][y:y+3]
            for k in (0,1,2)), []) for x in (0,3,6) for y in (0,3,6)]:
        if len(set(l)) < 9: return 'Try again!'
    return 'Finished!'
