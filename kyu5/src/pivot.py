from collections import defaultdict
from operator import itemgetter, attrgetter

def create_pivot(report, index):
    """Create a dict based on input 2d array."""
    d = defaultdict(list)
    for i in range(len(report[0])):
        for j in range(len(report)):
            key = report[j][index]
            try:
                d[key].append(coerce(report[j][i]))
            except ValueError:
                continue
    return d


def coerce(s):
    """Return a float or an integer number if input string is a number."""
    try:
        s = int(s)
        return int(s)
    except ValueError:
        s = float(s)
        return float(s)


def get_num_cols(report):
    """Return the count of columns which contain numbers."""
    num_cols = 0
    for val in report[0]:
        try:
            coerce(val)
            num_cols += 1
        except ValueError:
            pass
    return num_cols


def chunks(l, n):
    """Yield successive n-sized chunks from given list."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def pivot(report, index):
    """Return a 2d array based on an input dictionary and an index to group by."""
    d = create_pivot(report, index)
    num_cols = get_num_cols(report)
    out = []
    for k, v in d.items():
        line_out = []
        nums = chunks(v, len(v) // num_cols)
        for idx, val in enumerate(report[0]):
            try:
                coerce(val)
                line_out.append(float(sum(next(nums))))
            except ValueError:
                if idx == index:
                    line_out.append(k)
                else:
                    line_out.append('-')
        out.append(line_out)
    return sorted(out, key=itemgetter(index))
