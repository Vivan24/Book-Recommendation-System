from src.recsys import similarity

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
    
    num_books = 53
    num_users = 32

    books = open("../data/books.txt", "r")
    

    rating_matrix = []
    user_vector = []

    # stores all ratings of users in a matrix
    with open("../test-data/small-test-ratings.txt", "r") as scores:
        for rating in scores:
            if rating.strip().startswith("User"):
                rating_matrix.append(user_vector)
                user_vector = []
            else:
                user_vector.append(int(rating.strip()))
        
        rating_matrix.append(user_vector)
        rating_matrix.pop(0)

    #print(rating_matrix)

if __name__ == "__main__":
    main()




