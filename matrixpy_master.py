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
        
        self.elements = nested_lst_rows

class MatrixCols(Matrix):
    def __init__(self, num_rows = 0, num_cols = 0, **kwargs):
        super().__init__(**kwargs)
        # run method convert_col() to organize by columns
        self.set_col()

    def set_col(self):
        # initialize empty nested list that can be updated individually
        # (Prof Bemis showed us how to do this in lecture one day)
        nested_lst_col = [[] for i in range(self.num_cols)]

        i = 0
        j = 0

        print(len(nested_lst_col[i]))

        while j < len(self.elements):
            while len(nested_lst_col[i]) < self.num_rows:
                nested_lst_col[i].append(self.elements[j])
                j += num_cols
                print(j)
            i += 1
            print(i)

        self.elements = nested_lst_col


elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_rows = MatrixRows(elements=elements, num_rows=3, num_cols=3)
test_cols = MatrixCols(elements=elements, num_rows=3, num_cols=3)

#print(test_rows.elements) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(test_cols.elements) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

