#!/usr/bin/python 
def matrix_divided(matrix, div):
    error = "matrix must be a matrix (list of lists) of integers/floats"
                                            error2 = "Each row of the matrix must have the same size"

                                                if not isinstance(matrix, list):
                                                        raise TypeError(f"{error}")
                                                            elif all(isinstance(value, list) for value in matrix) is False:
                                                                    raise TypeError(f"{error}")
                                                                        elif all(len(value) == len(matrix[0]) for value in matrix) is False:
                                                                                raise TypeError(f"{error2}")
                                                                                    new = [isinstance(num, (int, float)) for val in matrix for num in val]
                                                                                        if all(new) is False:
                                                                                                raise TypeError(f"{error}")
                                                                                                    elif not isinstance(div, (int, float)):
                                                                                                            raise TypeError("div must be a number")
                                                                                                                elif div == 0:
                                                                                                                        raise ZeroDivisionError("division by zero")
                                                                                                                            else:
                                                                                                                                    a = map(lambda s: list(map(lambda x: round(x / div, 2), s)), matrix)
                                                                                                                                            return list(a)
