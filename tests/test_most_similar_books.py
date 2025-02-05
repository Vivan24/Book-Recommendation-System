import sys
from pathlib import Path

# Add project root to sys.path
ROOT = Path(__file__).parent.parent
sys.path.append(str(ROOT))

import config

from src.most_similar_books import main
import os

def test_most_similar_books_main():
    """
    The correct answers. Do NOT edit the 
    most-similar-books-correct-answer.txt file 
    or you will mess up this test!
    """

    correct_file = config.TEST_CORRECT_DATA.open("r")

    main() # when main runs, it should write out most-similar-books.txt
    actual_output_filename = config.DATA_OUTPUT
    actual_file = open(actual_output_filename, "r")

    # reads both files side by side and checks if each line is exactly the same
    correct_line = correct_file.readline()
    actual_line = actual_file.readline()
    while correct_line != "":
        assert correct_line == actual_line
        correct_line = correct_file.readline()
        actual_line = actual_file.readline()         

    correct_file.close()
    actual_file.close()
    os.remove( actual_output_filename )
   
