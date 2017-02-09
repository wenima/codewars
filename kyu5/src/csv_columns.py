csv = 'a,b,c,d,e\n1,2,3,4,5\nf,g,h,i,j'
indeces = [1, 3, 5, 7]

def csv_columns(csv, indeces):
    indeces = sorted(set(indeces))
    #split csv into lists
    ld = [l.split(',') for l in csv.splitlines()]
    #generate list of output strings
    out_csv = []
    for l in ld:
        for i in indeces:
            if i >= len(ld[0]):
                break
            out_csv.append(l[i])
            out_csv.append(',')
        if len(out_csv):
            out_csv[-1] = '\n'
    if len(out_csv):
        del out_csv[-1]
    return ''.join(out_csv) if out_csv else ""
