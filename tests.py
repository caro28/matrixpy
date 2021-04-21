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

# TODO: build instance and then unittest
def test_MatrixSparse_instance():
    x = MatrixSparse(elements=[], num_rows=0, num_cols=0)

    # set elements, num_rows, num_cols
    lst_elements = [0, 0, 0, 3, 0, 0, 5, 0, 3]
    x.set_elements(lst_elements)
    x.set_numrows(3)
    x.set_numcols(3)

    '''
    test case example:
    y = MatrixSparse(elements=[0, 0, 0, 3, 0, 0, 5, 0, 3], num_rows=3, num_cols=3)
    self.assertEqual(x.elements, {(1, 0): 3, (2, 0): 5, (2, 2): 3})
    '''
    
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
        self.assertEqual(x.change_matrix_shape(MatrixCols).get_elements(), [[1, 4, 7], [2, 5, 8], [3, 6, 9]]) # >> REVIEW
    
    def test_getelement(self):
        x = test_Matrix_instance()
        self.assertEqual(x.get_element(2,2), 9)

    def test_transpose(self):
        x = test_MatrixRows_instance()
        self.assertEqual(x.transpose().get_elements(), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    
    def test_addmatrix(self):
        x = test_Matrix_instance()
        other = test_MatrixRows_instance()
        self.assertEqual(x.add_matrix(other, MatrixCols).get_elements(), [[2, 8, 14], [4, 10, 16], [6, 12, 18]])

    def test_subtractmatrix(self):
        x = test_Matrix_instance()

    def test_scalar_multiply(self):
        x = test_Matrix_instance()

    def test_scalar_divide(self):
        x = test_Matrix_instance()

    def test_slicematrix(self):
        x = test_Matrix_instance()

    def test_docproduct(self):
        x = test_Matrix_instance()    

    def test_multiplymatrix(self):
        x = test_Matrix_instance()

    def test_multiplymmatrix(self):
        x = test_Matrix_instance()                              


class TestMatrixRows(unittest.TestCase):
    '''
    Do not test set_elements(self) because set_rows() has already been called
    '''
    # TODO-question: not needed b/c already tested in parent class?
    def test_setnumrows(self):
        x = test_MatrixRows_instance()
        self.assertEqual(x.num_rows, 3)
    
    # TODO-question: not needed b/c already tested in parent class?
    def test_setnumcols(self):
        x = test_MatrixRows_instance()
        self.assertEqual(x.num_cols, 3)

    # TODO-question: not needed b/c already tested in parent class?
    def test_getelements(self):
        x = test_MatrixRows_instance()
        self.assertEqual(x.get_elements(), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_setrows(self):
        x = test_MatrixRows_instance()
        self.assertEqual(x.elements, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_getsimplelst(self):
        x = test_MatrixRows_instance()
        self.assertEqual(x.elements, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])    



class TestMatrixCols(unittest.TestCase):
    '''
    Do not test set_elements(self) because set_cols() has already been called
    '''
    # TODO-question: not needed b/c already tested in parent class?
    def test_setnumrows(self):
        x = test_MatrixCols_instance()
        self.assertEqual(x.num_rows, 3)
    
    # TODO-question: not needed b/c already tested in parent class?
    def test_setnumcols(self):
        x = test_MatrixCols_instance()
        self.assertEqual(x.num_cols, 3)

    # TODO-question: not needed b/c already tested in parent class?
    def test_getelements(self):
        x = test_MatrixCols_instance()
        self.assertEqual(x.get_elements(), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_setcols(self):
        x = test_MatrixCols_instance()
        self.assertEqual(x.elements, [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_getsimplelst(self):
        x = test_MatrixCols_instance()
        self.assertEqual(x.elements, [[1, 4, 7], [2, 5, 8], [3, 6, 9]]) 
          


class TestMatrixSparse(unittest.TestCase):

    def test_setdict(self):
        x = test_MatrixSparse_instance()
        self.assertEqual(x.elements, {(1, 0): 3, (2, 0): 5, (2, 2): 3})


    



if __name__ == "__main__":
    unittest.main(verbosity = 2)


