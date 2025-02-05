# Book Recommendation System

## Overview
This project implements a book recommendation system using **cosine similarity** to find the most similar books based on given data. It includes:
- Implementation of cosine similarity in Python.
- Unit testing with `pytest`.
- A script to compute and output the most similar book for each book in the dataset.
- A structured GitHub repository following best practices.

## File Structure
```
├── data/
│   ├── books.txt                           # Input file with book data
|   ├── ratings.txt                         # Input file with user ratings data
│   ├── output-similar-books.txt            # Output file (created when run) with computed recommendations
│
├── src/
│   ├── recsys.py                           # Implementation of cosine similarity
│   ├── most_similar_books.py               # Script to compute most similar books
│
├── tests
|   ├── test-data
|      ├── most-similar-books-correct-answer.txt
|      ├── output-similar-books-test.txt
|      ├── most-similar-books-correct-answer.txt
|      ├── small-test-books.txt
|      ├── small-test-ratings.txt
|   ├── test_most_similar_books.py          # Tests for the main script
|   ├── test_recsys.py                      # Tests for cosine similarity logic
|
├── config.py                               # Holds all file paths with pathlib
├── gitignore.txt                           
└── README.md                               # Project documentation
```

## Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. **Run the recommendation system:**
   ```sh
   python src/most_similar_books.py
   ```
   This generates `output-similar-books.txt` with the most similar book for each entry.

2. **Run tests:**
   ```sh
   pytest src/test_recsys.py
   test_most_similar_books.py
   ```
   This ensures cosine similarity and comparing book logic works correctly.

## How It Works
1. `recsys.py` implements **cosine similarity** to compute the similarity between books based on their feature vectors.
2. `most_similar_books.py` reads the book dataset, calculates pairwise similarity, and finds the closest match for each book.
3. `test_recsys.py` contains **unit tests** to validate the correctness of the similarity function.
4. `test_most_similar_books.py` compares answer file and output file to validate the correctness of the program.
5. The results are saved in `output-similar-books.txt`.

## License
This project is for educational purposes. Feel free to modify and experiment with it.

