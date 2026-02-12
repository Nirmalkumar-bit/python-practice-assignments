# Task: Implement validate_matrix(matrix).
# Requirements:
# - matrix must be a non-empty list of non-empty lists
#   If invalid type/emptiness, raise TypeError("matrix must be a non-empty list of non-empty lists")
# - All rows must have the same length; else ValueError("matrix rows must have the same length")
# - All elements must be numbers (int/float, bool not allowed); else TypeError("matrix elements must be numbers")
# - Return (rows, cols)
# Expected outcome:
# - validate_matrix([[1,2],[3,4]]) returns (2,2)
# - validate_matrix([[1,2],[3]]) raises ValueError("matrix rows must have the same length")


def validate_matrix(matrix):
     if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a non-empty list of non-empty lists")
    
    # Check each row is a non-empty list
     for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a non-empty list of non-empty lists")
    
    # Check all rows same length
     cols = len(matrix[0])
     for row in matrix:
        if len(row) != cols:
            raise ValueError("matrix rows must have the same length")
    
    # Check all elements are numbers (no bool)
     for row in matrix:
        for value in row:
            if type(value) not in (int, float):
                raise TypeError("matrix elements must be numbers")
    
     return (len(matrix), cols)
    # TODO
    


if __name__ == "__main__":
    print(validate_matrix([[1, 2], [3, 4]]))