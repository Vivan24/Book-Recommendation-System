from recsys import similarity

# Do not change this function.  You must use this function.
def format_similar_message(source_book_title, 
                           most_similar_title, 
                           similarity_score):
    """Function to produce a properly formatted string for output most similar book."""
    result = f'People who liked {source_book_title}, ' + \
             f'also liked {most_similar_title}. (Score = {similarity_score:.3f})'
    return result

# add functions you write below and then delete this comment.





def main():
    """
    For each book in books.txt, this program outputs to the file 
    most-similar-books.txt the book and the book that is most similar 
    to it given the cosine similarity between it and all other books
    using the ratings in ratings.txt. This program does not prompt
    the user for any input. For more details, see the homework assignment.
    """
    # add your code below and then delete this comment.
    
    num_books = 53
    num_users = 32

    books = open("books.txt", "r")
    scores = open("ratings.txt", "r")

    rating_matrix = []
    user_vector = []

    # stores all ratings of users in a matrix
    for rating in scores:
        if rating.startswith("User") and rating > 0:
            rating_matrix.append(user_vector)
            user_vector = []
        else:
            user_vector.append(int(rating.strip()))

    for book in books:
        


if __name__ == "__main__":
    main()




