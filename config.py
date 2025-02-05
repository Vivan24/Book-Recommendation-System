from pathlib import Path

# Project root
ROOT = Path(__file__).parent

# 'data' folder
DATA_DIR = ROOT / "data"
DATA_RATINGS = DATA_DIR / "ratings.txt"
DATA_BOOKS = DATA_DIR / "books.txt"
DATA_OUTPUT = DATA_DIR / "output-similar-books.txt"

# 'test-data' folder
TEST_DATA_DIR = ROOT / "tests" / "test-data"
TEST_DATA_BOOKS = TEST_DATA_DIR / "small-test-books.txt"
TEST_DATA_RATINGS = TEST_DATA_DIR / "small-test-ratings.txt"
TEST_DATA_OUTPUT = TEST_DATA_DIR / "output-similar-books-test.txt"
TEST_CORRECT_DATA = TEST_DATA_DIR / "most-similar-books-correct-answer.txt"