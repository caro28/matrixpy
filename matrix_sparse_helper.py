from math import floor

def convert_tuple(elem_indices, num_cols):
    '''
    Converts list of indices to tuples of (row, column) values, indicating
    position in a matrix.
    Parameters:
        elem_indices: (list) index of matrix element from original list of
        elements, used when creating Matrix instance
        num_cols: (int) number of columns in original matrix
    Returns:
        row_col_lst: (list) list of (row, col) tuples
    '''
    # get row numbers from elem_indices
    row_num = []
    for i in range(len(elem_indices)):
        if elem_indices[i] < num_cols:
            row_num.append(0)
        elif elem_indices[i] == num_cols:
            row_num.append(1)
        else:
            row = floor(elem_indices[i] / num_cols)
            row_num.append(row)
        
    # get col numbers from elem_indices
    col_num = []
    for index in elem_indices:
        if index < num_cols:
            col_num.append(index)
        else:
            col = index % num_cols
            col_num.append(col)

    # combine row number, col number into tuples
    row_col_lst = tuple(zip(row_num, col_num))

    return row_col_lst