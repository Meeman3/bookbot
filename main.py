from stats import word_count

def get_books_text(file_path):
    
    with open(file_path) as p:

        file_contents = p.read()

        return file_contents
    
def main():

    book_words = get_books_text("books/frankenstein.txt")

    print(f"{word_count(book_words)} words found in the document")




main()