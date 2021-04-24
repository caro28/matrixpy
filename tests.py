# Prof Bemis said that how we organize the tests is up to us. What I've done 
# is write a test per method, where possible

from matrixpy_master import Matrix, MatrixRows, MatrixCols, MatrixSparse
import unittest

def test_Matrix_instance():
    # create Matrix instance
    x = Matrix(elements=[], num_rows=0, num_cols=0)

    # set elements, num_rows, num_cols
    lst_elements = [i for i in range(1, 10)]
    x.set_elements(lst_elements)
    x.set_numrows(3)
    x.set_numcols(3)

    return x

def test_MatrixSparse_instance():
    x = MatrixSparse(elements=[], num_rows=0, num_cols=0)

    # set elements, num_rows, num_cols
    lst_elements = [0, 0, 0, 3, 0, 0, 5, 0, 3]
    x.set_elements(lst_elements)
    x.set_numrows(3)
    x.set_numcols(3)
    
    # organize non-zero elements by key/values (dict)
    x.set_dict()
    
    return x

def test_MatrixRows_instance():
    x = MatrixRows(elements=[], num_rows = 0, num_cols = 0)
    # set elements, num_rows, num_cols
    lst_elements = [i for i in range(1, 10)]
    x.set_elements(lst_elements)
    x.set_numrows(3)
    x.set_numcols(3)

    # organize elements by rows
    x.set_rows()

    return x

def test_MatrixCols_instance():
    x = MatrixCols(elements=[], num_rows = 0, num_cols = 0)
    # set elements, num_rows, num_cols
    lst_elements = [i for i in range(1, 10)]
    x.set_elements(lst_elements)
    x.set_numrows(3)
    x.set_numcols(3)

    # organize elements by rows
    x.set_cols()

    return x


class TestMatrix(unittest.TestCase):

    def test_setelements(self):
        x = test_Matrix_instance()
        self.assertEqual(x.elements, [i for i in range(1, 10)])

    def test_getelements(self):
        x = test_Matrix_instance()
        self.assertEqual(x.get_elements(), [i for i in range(1, 10)])
    
    def test_setnumrows(self):
        x = test_Matrix_instance()
        self.assertEqual(x.num_rows, 3)
    
    def test_setnumcols(self):
        x = test_Matrix_instance()
        self.assertEqual(x.num_cols, 3)
    
    def test_getnumrows(self):
        x = test_Matrix_instance()
        self.assertEqual(x.get_numrows(), 3)

    def test_getnumcols(self):
        x = test_Matrix_instance()
        self.assertEqual(x.get_numcols(), 3)   

    def test_changematrixshape(self):
        x = test_Matrix_instance()
        self.assertEqual(x.change_matrix_shape(MatrixCols).get_elements(), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        self.assertEqual(x.change_matrix_shape(MatrixRows).get_elements(), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(x.change_matrix_shape(MatrixSparse).get_elements(), {(0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 9})
    
    def test_getvalue(self):
        x = test_Matrix_instance()
        self.assertEqual(x.get_value(2,2), 9)

    def test_transpose(self):
        x = test_MatrixRows_instance()
        self.assertEqual(x.transpose().get_elements(), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    
    def test_addmatrix(self):
        x1 = test_Matrix_instance()
        x2 = test_MatrixSparse_instance()
        other1 = test_MatrixRows_instance()
        other2 = test_MatrixCols_instance()
        other3 = test_MatrixSparse_instance()
        self.assertEqual(x1.add_matrix(other1).get_elements(), [[2, 4, 6], [8, 10, 12], [14, 16, 18]])
        self.assertEqual(x2.add_matrix(other2).get_elements(), [[1, 2, 3], [7, 5, 6], [12, 8, 12]])
        self.assertEqual(x1.add_matrix(other3).get_elements(), [[1, 2, 3], [7, 5, 6], [12, 8, 12]])

    def test_subtractmatrix(self):
        x1 = test_Matrix_instance()
        x2 = test_MatrixSparse_instance()
        other1 = test_MatrixRows_instance()
        other2 = test_MatrixCols_instance()
        other3 = test_MatrixSparse_instance()
        self.assertEqual(x1.subtract_matrix(other1).get_elements(), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(x2.subtract_matrix(other2).get_elements(), [[-1, -2, -3], [-1, -5, -6], [-2, -8, -6]])
        self.assertEqual(x1.subtract_matrix(other3).get_elements(), [[1, 2, 3], [1, 5, 6], [2, 8, 6]])

    def test_scalar_multiply(self):
        x1 = test_Matrix_instance()
        x2 = test_MatrixSparse_instance()
        x3 = test_MatrixRows_instance()
        x4 = test_MatrixCols_instance()
        self.assertEqual(x1.scalar_multiply(-1).get_elements(), [-1, -2, -3, -4, -5, -6, -7, -8, -9])
        self.assertEqual(x2.scalar_multiply(2).get_elements(), {(1, 0): 6, (2, 0): 10, (2, 2): 6})
        self.assertEqual(x3.scalar_multiply(0).get_elements(), [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.assertEqual(x4.scalar_multiply(-2).get_elements(), [[-2, -8, -14], [-4, -10, -16], [-6, -12, -18]])

    def test_scalar_divide(self):
        x1 = test_Matrix_instance()
        x2 = test_MatrixSparse_instance()
        x3 = test_MatrixRows_instance()
        x4 = test_MatrixCols_instance()
        self.assertEqual(x1.scalar_divide(-1).get_elements(), [-1, -2, -3, -4, -5, -6, -7, -8, -9])
        self.assertEqual(x2.scalar_divide(2).get_elements(), {(1, 0): 1.5, (2, 0): 2.5, (2, 2): 1.5})
        self.assertEqual(x3.scalar_divide(1).get_elements(), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(x4.scalar_divide(-2).get_elements(), [[-0.5, -2, -3.5], [-1, -2.5, -4], [-1.5, -3, -4.5]])

    def test_slicematrix(self):
        x1 = test_Matrix_instance()
        x2 = test_MatrixSparse_instance()
        x3 = test_MatrixRows_instance()
        x4 = test_MatrixCols_instance()
        self.assertEqual(x1.slice_matrix(0, 2, 1, 2), [[2, 3, 4], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(x2.slice_matrix(1, 2, 1, 2), {(2, 2): 3})
        self.assertEqual(x3.slice_matrix(2, 2, 0, 2), [7, 8, 9])
        self.assertEqual(x4.slice_matrix(0, 0, 1, 2), [2, 3])

    def test_dotproduct(self):
        x1 = test_Matrix_instance()
        x2 = test_MatrixSparse_instance()
        x3 = test_MatrixRows_instance()
        slice1 = x1.slice_matrix(0, 0, 0, 2)
        slice2 = x2.slice_matrix(2, 2, 0, 2)
        slice3 = x3.slice_matrix(0, 2, 1, 1)
        self.assertEqual(x1.dot_product(slice1, slice3, 0, 0, x1.num_cols, 0, 1, x3.num_rows), 36)
        self.assertEqual(x2.dot_product(slice2, slice3, 2, 0, x2.num_cols, 0, 1, x3.num_rows), 34)

    def test_multiplymatrix(self):
        x1 = test_Matrix_instance()
        x2 = test_MatrixSparse_instance()
        x3 = test_MatrixRows_instance()
        x4 = test_MatrixCols_instance()
        self.assertEqual(x1.multiply_matrix(x3).get_elements(), [[30, 36, 42], [66, 81, 96], [102, 126, 150]])
        self.assertEqual(x2.multiply_matrix(x4).get_elements(), [[0, 0, 0], [3, 6, 9], [26, 34, 42]])


class TestMatrixSparse(unittest.TestCase):
    def test_setdict(self):
        x = test_MatrixSparse_instance()
        self.assertEqual(x.elements, {(1, 0): 3, (2, 0): 5, (2, 2): 3})

    def test_getdctlst(self):
        x = test_MatrixSparse_instance()
        self.assertEqual(x.get_dct_lst(), [0, 0, 0, 3, 0, 0, 5, 0, 3])
    
    def test_changematrixshape(self):
        x = test_MatrixSparse_instance()
        y = test_MatrixSparse_instance()
        self.assertEqual(x.change_matrix_shape(MatrixCols).get_elements(), [[0, 3, 5], [0, 0, 0], [0, 0, 3]])
        self.assertEqual(y.change_matrix_shape(MatrixRows).get_elements(), [[0, 0, 0], [3, 0, 0], [5, 0, 3]])


class TestMatrixRows(unittest.TestCase):
    '''
    Do not test set_elements(self) because set_rows() has already been called
    '''
    def test_setrows(self):
        x = test_MatrixRows_instance()
        self.assertEqual(x.elements, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_getsimplelst(self):
        x = test_MatrixRows_instance()
        self.assertEqual(x.get_simple_lst(), [i for i in range(1, 10)])    

    def test_changematrixshape(self):
        x = test_MatrixRows_instance()
        self.assertEqual(x.change_matrix_shape(MatrixCols).get_elements(), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
        self.assertEqual(x.change_matrix_shape(MatrixSparse).get_elements(), {(0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 9})


class TestMatrixCols(unittest.TestCase):
    '''
    Do not test set_elements(self) because set_cols() has already been called
    '''
    def test_setcols(self):
        x = test_MatrixCols_instance()
        self.assertEqual(x.elements, [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_getsimplelst(self):
        x = test_MatrixCols_instance()
        self.assertEqual(x.get_simple_lst(), [i for i in range(1, 10)])
    
    def test_changematrixshape(self):
        x = test_MatrixCols_instance()
        self.assertEqual(x.change_matrix_shape(MatrixRows).get_elements(), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(x.change_matrix_shape(MatrixSparse).get_elements(), {(0, 0): 1, (0, 1): 2, (0, 2): 3, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 7, (2, 1): 8, (2, 2): 9})
    

if __name__ == "__main__":
    unittest.main(verbosity = 2)


