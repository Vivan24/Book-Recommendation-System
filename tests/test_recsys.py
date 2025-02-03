import math
from src.recsys import similarity

def test_similarity_no_ratings():
    """
    This test sends a vector with all zeros into recsys.similarity and
    verifies that the result is 0.0.  The test checks many different 
    lengths of vectors (typical vector lengths of 1 to 3).  The test is 
    careful to check both vectors being all zeros, and one vector 
    being all zeros with the other vector not being all zeros.  
    """

    assert math.isclose(similarity([0], [0]), 0.0, abs_tol=0.0001)
    assert math.isclose(similarity([1], [0]), 0.0, abs_tol=0.0001)
    assert math.isclose(similarity([0], [1]), 0.0, abs_tol=0.0001)
    assert math.isclose(similarity([0, 0], [0, 0]), 0.0, abs_tol=0.0001)
    assert math.isclose(similarity([1, 2], [0, 0]), 0.0, abs_tol=0.0001)
    assert math.isclose(similarity([0, 0], [-2, -2]), 0.0, abs_tol=0.0001)
    assert math.isclose(similarity([0, 0, 0], [0, 0, 0]), 0.0, abs_tol=0.0001)
    assert math.isclose(similarity([2, 1, -1], [0, 0, -0]), 0.0, abs_tol=0.0001)
    assert math.isclose(similarity([0, 0, 0], [1, -1, -2]), 0.0, abs_tol=0.0001)
    assert math.isclose(similarity([0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]), 0.0, abs_tol=0.0001)
    assert math.isclose(similarity([9, 2, 5, 6, 2, 1, 7], [0, 0, 0, 0, 0, 0, 0]), 0.0, abs_tol=0.0001)
    assert math.isclose(similarity([0, 0, 0, 0, 0, 0, 0], [9, 1, 2, 3, 5, 6, 1]), 0.0, abs_tol=0.0001)

def test_similarity_identical_books():
    """
    This test sends two identical vectors to the recsys.similarity function
    and asserts that the similarity is reported to be 1.0 within a tolerance of
    0.0001.  The test checks many different vectors and lengths of vectors
    (typical vector lengths of 1 to 3).  Note that an all zero vector has 
    a similarity of zero with itself and not similarity of 1.
    """
    # To test that two numbers, actual and expected, are within 0.0001 of
    #  each other, do:
    #  assert math.isclose(actual, expected, abs_tol=0.0001)
    #
    # For more info: https://docs.python.org/3/library/math.html#math.isclose
    #
    # Add your code below.  When done, delete this comment.

    assert math.isclose(similarity([1], [1]), 1.0, abs_tol=0.0001)
    assert math.isclose(similarity([1, 2], [1, 2]), 1.0, abs_tol=0.0001)
    assert math.isclose(similarity([1, 2, 3], [1, 2, 3]), 1.0, abs_tol=0.0001)
    assert math.isclose(similarity([9, 2, 5, 6, 2, 1, 7], [9, 2, 5, 6, 2, 1, 7]), 1.0, abs_tol=0.0001)

def test_similarity_diff_books():
    """
    This test sends two different vectors to the recsys.similarity function
    and asserts that the similarity is reported to be within a tolerance of
    0.0001 of the hand computed cosine similarity.  The test checks many 
    different vector pairs and lengths of vectors (typical vector lengths of
    1 to 3).
    """

    assert math.isclose(similarity([5], [3]), 1.0, abs_tol=0.0001)
    assert math.isclose(similarity([-1, -1], [-2, -2]), 1.0, abs_tol=0.0001)
    assert math.isclose(similarity([2, 1, -1], [1, -1, -2]), 0.5, abs_tol=0.0001)
    assert math.isclose(similarity([6, 1, -1, 10, 23], [1, -1, -2, 5, 7]), 0.943732, abs_tol=0.0001)

    # Checking if rigorously correct by seeing it handle vectors in ℝ^32 (32-dimensions)
    assert math.isclose(similarity([-5, 7, 9, 8, 8, -8, -10, 10, 8, -1, 10, 1, -10, -4, 9, -5, -10, -7, 5, 9, 5, 5, -9, -10, 4, -2, 4, -6, 7, -10, 3, 7], [8, -7, -2, 8, 6, 3, -5, -8, -3, -9, -6, -8, 0, -7, -3, 7, 9, 3, 7, -8, 9, -2, 9, 0, -3, 5, 6, -7, 9, -4, 0, 6]), -0.1181109, abs_tol=0.0001)