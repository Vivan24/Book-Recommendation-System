import math

"""
This module contains functions for building 
recommendation systems.
"""

def similarity(vector1, vector2):
    """
    Returns the cosine similarity between two vectors.  The vectors
    must have the same length.  If either vector is all zeros, then the
    similarity is defined to be zero.  Vectors are assumed to be lists that
    contain numbers (ints and floats).
    """
    if len(vector1) != len(vector2):
        raise ValueError("vectors must be same length")

    dot_product = 0
    norm_x = 0
    norm_y = 0

    for i in range(len(vector1)):
        dot_product += vector1[i] * vector2[i]
        norm_x += vector1[i] ** 2
        norm_y += vector2[i] ** 2

    if (norm_x == 0) or (norm_y == 0):
        return 0.0

    norm = (norm_x ** (1/2)) * (norm_y ** (1/2)) # Where 'n' raised to '1/2' is the same as square root
    similarity_value = dot_product / norm

    return similarity_value
