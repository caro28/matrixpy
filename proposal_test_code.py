class Matrix:
    def __init__(self, elements = []):
        self.elements = elements
    
    def set_elements(self, lst_elements):
        # lst_elements is a nested list, organized by rows
        lst_elements = self.elements

class MatrixRows(Matrix):
    def __init__(self, num_rows = 0, num_cols = 0, **kwargs):
        super().__init__(**kwargs)
        self.num_rows = num_rows
        self.num_cols = num_cols

class MatrixCols(Matrix):
    def __init__(self, num_rows = 0, num_cols = 0, **kwargs):
        super().__init__(**kwargs)
        self.num_rows = num_rows
        self.num_cols = num_cols
        # run method convert_col() in order to organize by columns
        self.convert_col()

    def convert_col(self):
        # initialize empty nested list that can be updated individually
        # (Prof Bemis showed us how to do this in lecture one day)
        nested_lst_col = [[] for i in range(len(self.elements))]

        i = 0
        j = 0

        while i < len(self.elements):
            while j < (len(self.elements[i])):
                nested_lst_col[i].append(self.elements[j][i])
                j += 1
            i += 1
            j = 0

        self.elements = nested_lst_col


nested_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
test_rows = MatrixRows(elements=nested_lst, num_rows=0, num_cols=0)
test_cols = MatrixCols(elements=nested_lst, num_rows=0, num_cols=0)

print(test_rows.elements) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(test_cols.elements) # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

