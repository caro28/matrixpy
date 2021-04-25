## MatrixPy

MatrixPy is a package designed to represent matrices of various dimensions, along with main matrix operations such as addition, subtraction, scalar multiplication, scalar division, dot product, matrix multiplication and transposition.


## Installation

Please make sure you have the latest 3.x version from [python.org](https://www.python.org/)

1. On the main page of this repo, click on the "code" button right above the list of files.
2. Copy the link provided in the textbox.
3. In your terminal, select the location where you want the cloned repo to be
4. Type `git clone`, and then paste the URL you copied earlier.
5. Press **Enter**.


## How to Use
This package allows you to work with n-dimensional matrices using arrays as inputs, and organize them by rows or columns using MatrixRows and MatrixCols subclasses, respectively, to provide this functionality. These subclasses will transform the input array into nested lists, using indexing based on the matrix's dimensions. A nice feature of this package is the MatrixSparse subclass, where non-zero elements only are stored in a dictionary, saving space in memory.

The main operations available in this package are under the Matrix parent class:

1. change_matrix_shape(): changes the shape of the matrix; return new matrix object
2. get_value(): access a matrix element
3. transpose(): swap rows and columns of matrix; return a new matrix instance
4. add_matrix(): add two matrix instances; return a new matrix instance
5. subtract_matrix(): subtract two matrix instances from each other; return a new matrix instance
6. scalar_multiply(): multiply a matrix by a scalar number; return a new matrix instance
7. scalar_divide(): divide a matrix by a scalar; return a new matrix instance
8. slice_matrix(): slice matrix by rows and columns; return sliced elements as list
9. dot_product(): perform the dot product of a row and column; return a scalar
10. multiply_matrix(): multiply two matrix instances; return a new matrix instance

Matrix operations in this package are methods of the Matrix parent class. Subclasses will inherit these methods.

In addition, each subclass contains methods with implementations specific to that subclass. For example, change_matrix_shape() is in each subclass, with implementation specific to that subclass's underlying data structure. Other subclass methods are used to shape their underlying data structure.


## Support
If you would like to report any issues, please follow the instructions below:

1. On the main page of this repo, under the "Issues" tab, click on the "New issue" button.
2. Please provide us a detailed description of the issue.
3. Click on "Submit new issue" and we will get back to you as soon as we can.


## Roadmap
Ways to improve MatrixPy include adding more operations (e.g. calculate a matrix’s inverse and perform SVD) and adding a broadcasting functionality.


## Contributing
Contributions to this package are welcome! Please follow the instructions below:  
1. Clone repo and create a new branch.
2. Make necessary changes and test.
3. Submit Pull Request with comprehensive description of your changes.


## Authors
Caroline Craig  
Nabyla Tanaka


