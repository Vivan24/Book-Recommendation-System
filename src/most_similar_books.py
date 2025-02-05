import sys
from pathlib import Path

# Add project root to sys.path
ROOT = Path(__file__).parent.parent
sys.path.append(str(ROOT))

import config
from src.recsys import similarity
from itertools import zip_longest

def format_similar_message(source_book_title, 
                           most_similar_title, 
                           similarity_score):
    """Function to produce a properly formatted string for output most similar book."""
    result = f'People who liked {source_book_title}, ' + \
             f'also liked {most_similar_title}. (Score = {similarity_score:.3f})\n'
    return result


def make_matrix(ratings_path, books_path):
    """
    Reads through ratings.txt and books.txt files simultaneously and produces
    a 2D array of all user ratings for each book as well as a normal list for
    all book names and returns two tuples for both values (matrix & book names)
    """
    
    # initializes arrays
    matrix = []
    user_vector = []
    book_names = []

    # opens to read both ratings and book name files and adds data to arrays
    with ratings_path.open("r") as scores, books_path.open("r") as books:
        for ratings, names in zip_longest(scores, books, fillvalue=''):
            # formatted to append all data for current user before moving to next
            if ratings.strip().startswith("User"):
                matrix.append(user_vector)
                user_vector = []
            else:
                user_vector.append(int(ratings.strip()))
            book_names.append(names.strip())
        
        # cleans up array and adds last user data
        matrix.pop(0)
        matrix.append(user_vector)

    return matrix, book_names

def main():
    """
    For each book in books.txt, this program outputs to the file
    most-similar-books.txt the book and the book that is most similar
    to it given the cosine similarity between it and all other books
    using the ratings in ratings.txt. This program does not prompt
    the user for any input.
    """

    # pulls ratings and book names from function
    ratings_matrix, list_books = make_matrix(config.DATA_RATINGS, config.DATA_BOOKS)

    # catches error if there aren't two or more books
    if len(ratings_matrix[0]) < 2:
        print("ERROR: There must be two or more books' ratings for each user to compare in \"raitings.txt\" data file")
    else:
        # matrix for tracking name of most similar book and similarity value from comparisions
        similarity_matrix = []
        for i in range(len(ratings_matrix[0])):
            most_similar_score = -1
            for j in range(len(ratings_matrix[0])):
                # avoids comparing to itself
                if i != j:
                    # each colum represents a book in matrix
                    curr_col = [row[i] for row in ratings_matrix]
                    diff_col = [row[j] for row in ratings_matrix]
                    curr_score = similarity(curr_col, diff_col) # compare logic

                    # updates value until highest similarity score is saved
                    if curr_score > most_similar_score:
                        most_similar_score = curr_score
                        most_similar_book = list_books[j] # j is column index for each book

            # before moving to next book, adds most similar book's name and score
            similarity_matrix.append([most_similar_book, most_similar_score])

    # writes to the output file
    with config.DATA_OUTPUT.open("w") as output:
        for k in range(len(similarity_matrix)):
            output.write(format_similar_message(list_books[k], similarity_matrix[k][0], similarity_matrix[k][1]))

if __name__ == "__main__":
    main()