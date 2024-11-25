from typing import List, Tuple, Union

# Creating 'Matrix' suh that it accepts a list of lists, list of tuples, tuple of lists and a tuple of tuples
Matrix = Union[
    List[Union[List[Union[int, float, complex]], Tuple[Union[int, float, complex]]]],
    Tuple[Union[List[Union[int, float, complex]], Tuple[Union[int, float, complex]]]],
]


# Definition of a function to multiply the 2 given matrices
def matrix_multiply(matrix1: Matrix, matrix2: Matrix) -> Matrix:
    """
    Perform matrix multiplication
    Parameters:
    Matrix : Can contain a list of lists, a tuple of tuples, a list of tuples and a tuple of lists each which can consist of integers, floats and complex                    numbers
    Returns:
    Matrix : Obtained upon doing matrix multiplication

    """
    check_type(matrix1)
    check_type(matrix2)

    # Initialiazing the number of rows and columns
    rows1 = len(matrix1)
    cols1 = check_rows(matrix1)
    rows2 = len(matrix2)
    cols2 = check_rows(matrix2)

    # The number of columns in matrix1 must be equal to the number of rows of matrix2
    if cols1 != rows2:
        raise ValueError("Incompatible matrices for multiplication.")

    # Creating an array using list comprehension for the final result of matrix multiplication
    result = [[0] * cols2 for p in range(rows1)]

    # Performing matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            sum = 0
            for k in range(cols1):
                sum += matrix1[i][k] * matrix2[k][j]
            result[i][j] = sum

    return result


# Definition of a funcion which checks if each row has the same number of columns and then returns the value of the columns of the matrix is valid
def check_rows(matrix: Matrix) -> int:
    """
    Checks if each row consists of the same number of columns
    Parameters:
     Matrix : Can contain a list of lists, a tuple of tuples, a list of tuples and a tuple of lists each which can consist of integers, floats and complex                     numbers
    Returns:
    int : the number of columns in the matrix
    """
    if not len(matrix):
        raise ValueError("Empty matrices cannot be multiplied.")

        # initializing the number of columns
    num_cols = len(matrix[0])

    # To check if the number of each column matches with the number of columns of the first row
    for row in matrix:
        if len(row) != num_cols:
            raise ValueError("All rows must have the same number of columns.")
    return num_cols


# Definition of a function which checks the type of data in the given input
def check_type(matrix: Matrix) -> int:
    """
    Checks the data type of each row and element in the matrix
    Parameters:
    Matrix : Can contain a list of lists, a tuple of tuples, a list of tuples and a tuple of lists each which can consist of integers, floats and complex                    numbers
    """
    # if the given matrix is not a list or a tuple, an error is raised
    if not isinstance(matrix, (list, tuple)):
        raise TypeError("Matrix should be a list or tuple.")
    # if the row is not a list or a tuple, an error is raised
    for row in matrix:
        if not isinstance(row, (list, tuple)):
            raise TypeError("Each row should be a list or tuple.")
        # if an element is not a list or a tuple, an error is raised
        for element in row:
            if not isinstance(element, (int, float, complex)):
                raise TypeError("Matrix elements must be int, float, or complex.")
            # nan values in a matrix is an invalid input and since nan values are unequal this if statement is used
            if element != element:
                raise ValueError("nan values are not permitted")
            
# Corner cases:
# 1. The input given is not a list or a tuple
# 2. If each element in the matrix is a list or a tuple
# 3. If an element is nan 

# If matmul results don't match because of floating point rounding errors:
# My approach would be to import the decimal module and set the precision of all the numbers accordingly.
# To do that we can use the getcontext.prec()
# We can even change the rounding off method to our convenience.
