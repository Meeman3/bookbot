from stats import word_count, character_count, sort_dict, list_dict
import sys

#function that takes file path and returns contents of file
def get_books_text(file_path):
    
    with open(file_path) as p:

        file_contents = p.read()

        return file_contents
    
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_words = get_books_text(sys.argv[1])

    num_words = word_count(book_words)

    book_characters = character_count(book_words)

    d_list_sort = list_dict(book_characters)

    #print report of book using the functions
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(d_list_sort)):
        print (f"{d_list_sort[i]["char"]}: {d_list_sort[i]["num"]}")
    print("============= END ===============")





main()