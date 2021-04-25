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

1. change matrix shape: changes the shape of the matrix; return new matrix object
1. matrix addition: add two matrix instances; return a new matrix instance
2. matrix subtraction: subtract two matrix instances from each other; return a new matrix instance
3. scalar multiplication: multiply a matrix by a scalar number; return a new matrix instance
4. scalar division: divide a matrix by a scalar; return a new matrix instance
5. slice matrix: slice matrix by rows and columns; return sliced elements in a list
5. dot product: perform the dot product of a row and column; return a scalar
6. matrix multiplication: multiply two matrix instances; return a new matrix instance
7. matrix transposition: swap rows and columns of matrix; return a new matrix instance

Matrix operations in this package are methods of the Matrix parent class. Subclasses will inherit these methods.


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


