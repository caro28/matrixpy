from matrixpy_master import Matrix, MatrixRows, MatrixCols
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


# TODO: need to run tests for parent class methods in each subclass's test class?
class TestMatrixRows(unittest.TestCase):
    '''
    Do not test set_elements(self) because set_rows() has already been called
    '''

    def test_setnumrows(self):
        x = test_MatrixRows_instance()
        self.assertEquals(x.num_rows, 3)
    
    def test_setnumcols(self):
        x = test_MatrixRows_instance()
        self.assertEquals(x.num_cols, 3)

    def test_setrows(self):
        x = test_MatrixRows_instance()
        self.assertEquals(x.elements, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])


class TestMatrixCols(unittest.TestCase):
    '''
    Do not test set_elements(self) because set_cols() has already been called
    '''

    def test_setnumrows(self):
        x = test_MatrixCols_instance()
        self.assertEquals(x.num_rows, 3)
    
    def test_setnumcols(self):
        x = test_MatrixCols_instance()
        self.assertEquals(x.num_cols, 3)

    def test_setrows(self):
        x = test_MatrixCols_instance()
        self.assertEquals(x.elements, [[1, 4, 7], [2, 5, 8], [3, 6, 9]])




# TODO: how to run main function call?
unittest.main(verbosity = 5)

