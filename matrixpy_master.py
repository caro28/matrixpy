# TEST

class Matrix:
    def __init__(self, elements = [], num_rows = 0, num_cols = 0):
        self.elements = elements
        self.num_rows = num_rows
        self.num_cols = num_cols
    
    def set_elements(self, lst_elements):
        # lst_elements contains elements from row[0][0] to col[n][n]
        lst_elements = self.elements

class MatrixRows(Matrix):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # run method set_rows() to organize by rows
        self.set_rows()
    
    def set_rows(self):
        # created nested list with len = num_rows
        nested_lst_rows = [[] for i in range(self.num_rows)]

        i = 0
        j = 0

        while j < len(self.elements):
            while len(nested_lst_rows[i]) < self.num_cols:
                nested_lst_rows[i].append(self.elements[j])
                j += 1
            i += 1
            #print(i)
        
        self.elements = nested_lst_rows


class MatrixCols(Matrix):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # run method convert_col() to organize by columns
        self.set_cols()

    def set_cols(self):
        # initialize empty nested list that can be updated individually
        # (Prof Bemis showed us how to do this in lecture one day)
        nested_lst_cols = [[] for i in range(self.num_cols)]

        i = 0
        j = 0

        while j < len(self.elements):
            while len(nested_lst_cols[i]) < self.num_rows:
                nested_lst_cols[i].append(self.elements[j])
                j += self.num_cols
            i += 1

            if i < len(nested_lst_cols):
                # begin inner while loop at next index of self.elements
                j = i
            else:
                # end the while loop
                j = len(self.elements)

        self.elements = nested_lst_cols


