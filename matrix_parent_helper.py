def nstd_to_simple(x, num_rows, num_cols):
    '''
    Converts a nested list to a list. Helper function used in 
    matrixpy_master.py.
    Parameters:
        x: (list) nested list
        num_rows: (int) number of rows of original matrix
        num_cols: (int) number of columns of original matrix
    Returns:
        simple_lst: (list) elements in list
    '''
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
