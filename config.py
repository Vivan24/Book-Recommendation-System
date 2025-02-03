from pathlib import Path

# Project root
ROOT = Path(__file__).parent.parent 

# 'data' folder
DATA_DIR = ROOT / "data"
DATA_RATING = DATA_DIR / "ratings.txt"
DATA_BOOKS = DATA_DIR / "books.txt"

# 'test-data' folder
TEST_DATA_DIR = ROOT / "test-data"
TEST_DATA_BOOKS = TEST_DATA_DIR / "small-test-books.txt"
TEST_DATA_RATINGS = TEST_DATA_DIR / "small-test-ratings.txt"
CORRECT_DATA = TEST_DATA_DIR / "most-similar-books.txt"