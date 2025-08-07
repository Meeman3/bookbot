from stats import word_count
from stats import character_count

def get_books_text(file_path):
    
    with open(file_path) as p:

        file_contents = p.read()

        return file_contents
    
def main():

    book_words = get_books_text("books/frankenstein.txt")

    book_characters = character_count(book_words)

    print(f"{word_count(book_words)} words found in the document")

    print(book_characters)






main()