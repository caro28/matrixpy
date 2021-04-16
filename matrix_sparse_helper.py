from math import floor

def convert_tuple(elem_indices, num_cols):
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