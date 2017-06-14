"""Module to solve the code-kata https://www.codewars.com/kata/car-park-escape/."""

def escape(carpark):
    """Return a list of directions to take to escape a given carpark."""
    while True:
        try:
            carpark[0].index(2)
            break
        except:
            carpark = carpark[1:]
    if len(carpark) == 1:
        if carpark[0].index(2) + 1 == len(carpark[0]): return []
        return ["R" + str(len(carpark[-1]) - 1 - carpark[0].index(2))]
    out = []
    start = carpark[0].index(2)
    out, entry = find_exit(carpark[0], out, start)
    for row in carpark[1:-1]:
        out, entry = find_exit(row, out, entry)
    if entry + 1 != len(carpark[-1]):
        out.append("R" + str(len(carpark[-1]) - 1 - entry))
    return out

def find_exit(level, out, entry=0):
    """Return the escape route so far and the location of the stairs."""
    if level[entry] == 1:
        last_stairs = out[-1]
        new_stairs = "D" + str(int(last_stairs[-1]) + 1)
        out[-1] = new_stairs
        stairs = entry
    else:
        stairs = level.index(1)
        if stairs < entry:
            out.append("L" + str(entry - level.index(1)))
        else:
            out.append("R" + str(stairs - entry))
        out.append("D1")
    return out, stairs
