from stats import word_count, character_count, sort_dict, list_dict

def get_books_text(file_path):
    
    with open(file_path) as p:

        file_contents = p.read()

        return file_contents
    
def main():

    book_words = get_books_text("books/frankenstein.txt")

    num_words = word_count(book_words)

    book_characters = character_count(book_words)

    d_list_sort = list_dict(book_characters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(d_list_sort)):
        print (f"{d_list_sort[i]["char"]}: {d_list_sort[i]["num"]}")
    print("============= END ===============")





main()