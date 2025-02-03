import config
from src.recsys import similarity
from itertools import zip_longest

def format_similar_message(source_book_title, 
                           most_similar_title, 
                           similarity_score):
    """Function to produce a properly formatted string for output most similar book."""
    result = f'People who liked {source_book_title}, ' + \
             f'also liked {most_similar_title}. (Score = {similarity_score:.3f})'
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
    with config.TEST_DATA_RATINGS.open("r") as scores, config.TEST_DATA_BOOKS.open("r") as books:
        for ratings, names in zip_longest(scores, books, fillvalue=''):
            if ratings.strip().startswith("User"):
                ratings_matrix.append(user_vector)
                user_vector = []
            else:
                user_vector.append(int(ratings.strip()))

            book_names.append(names.strip())
        
        ratings_matrix.append(user_vector)
        ratings_matrix.pop(0)

    #print(rating_matrix)

if __name__ == "__main__":
    main()




