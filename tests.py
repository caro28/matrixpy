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
    '''
    test case example:
    y = MatrixSparse(elements=[0, 0, 0, 3, 0, 0, 5, 0, 3], num_rows=3, num_cols=3)
    self.assertEquals(x.elements, {(1, 0): 3, (2, 0): 5, (2, 2): 3})
    '''
    pass


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
        self.assertEquals(x.elements, [i for i in range(1, 10)])
    
    def test_setnumrows(self):
        x = test_Matrix_instance()
        self.assertEquals(x.num_rows, 3)
    
    def test_setnumcols(self):
        x = test_Matrix_instance()
        self.assertEquals(x.num_cols, 3)
    
    def test_getnumrows(self):
        x = test_Matrix_instance()
        self.assertEquals(x.get_numrows(), 3)
    
    def test_getelements(self):
        pass


class TestMatrixRows(unittest.TestCase):
    '''
    Do not test set_elements(self) because set_rows() has already been called
    '''
    # TODO-question: not needed b/c already tested in parent class?
    def test_setnumrows(self):
        x = test_MatrixRows_instance()
        self.assertEquals(x.num_rows, 3)
    
    # TODO-question: not needed b/c already tested in parent class?
    def test_setnumcols(self):
        x = test_MatrixRows_instance()
        self.assertEquals(x.num_cols, 3)

    def test_setrows(self):
        x = test_MatrixRows_instance()
        self.assertEquals(x.elements, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    def test_getelements(self):
        pass


class TestMatrixCols(unittest.TestCase):
    '''
    Do not test set_elements(self) because set_cols() has already been called
    '''
    # TODO-question: not needed b/c already tested in parent class?
    def test_setnumrows(self):
        x = test_MatrixCols_instance()
        self.assertEquals(x.num_rows, 3)
    
    # TODO-question: not needed b/c already tested in parent class?
    def test_setnumcols(self):
        x = test_MatrixCols_instance()
        self.assertEquals(x.num_cols, 3)

    def test_setcols(self):
        x = test_MatrixCols_instance()
        self.assertEquals(x.elements, [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_getelements(self):
        pass



if __name__ == "__main__":
    unittest.main(verbosity = 2)


