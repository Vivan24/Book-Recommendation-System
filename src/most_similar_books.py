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

def main():
    """
    For each book in books.txt, this program outputs to the file
    most-similar-books.txt the book and the book that is most similar
    to it given the cosine similarity between it and all other books
    using the ratings in ratings.txt. This program does not prompt
    the user for any input. For more details, see the homework assignment.
    """

    ratings_matrix = []
    user_vector = []
    book_names = []

    # stores all ratings of users in a matrix while saving all book names into an array
    with config.DATA_RATINGS.open("r") as scores, config.DATA_BOOKS.open("r") as books:
        for ratings, names in zip_longest(scores, books, fillvalue=''):
            if ratings.strip().startswith("User"):
                ratings_matrix.append(user_vector)
                user_vector = []
            else:
                user_vector.append(int(ratings.strip()))

            book_names.append(names.strip())
        
        ratings_matrix.append(user_vector)
        ratings_matrix.pop(0)

    # comparing books to one another
    if len(ratings_matrix[0]) < 2:
        print("ERROR: There must be two or more books' ratings for each user to compare in \"raitings.txt\" data file")
    else:
        similarity_matrix = []
        for i in range(len(ratings_matrix[0])):
            most_similar_score = -1
            for j in range(len(ratings_matrix[0])):
                if i != j:
                    curr_col = [row[i] for row in ratings_matrix]
                    diff_col = [row[j] for row in ratings_matrix]
                    curr_score = similarity(curr_col, diff_col)

                    if curr_score > most_similar_score:
                        most_similar_score = curr_score
                        most_similar_book = book_names[j]

            similarity_matrix.append([most_similar_book, most_similar_score])

    with config.DATA_OUTPUT.open("w") as output:
        for k in range(len(similarity_matrix)):
            output.write(format_similar_message(book_names[k], similarity_matrix[k][0], similarity_matrix[k][1]))

if __name__ == "__main__":
    main()