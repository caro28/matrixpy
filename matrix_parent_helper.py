
def nstd_to_simple(x, num_rows, num_cols):
    simple_lst = []
    i = 0
    j = 0

    while i < num_rows:
        while j < num_cols:
            simple_lst.append(x[i][j])
            j += 1
        i += 1
        j = 0
    
    return simple_lst
