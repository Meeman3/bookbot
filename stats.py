def word_count(book_words):

    word_list = book_words.split()

    num_words = len(word_list)

    return num_words

def character_count(book_words):

    count_dict = {}

    lower_letters = book_words.lower()

    for f in lower_letters:
            if f in count_dict:
                count_dict[f] += 1
            else:
                 count_dict[f] = 1
                 
    return count_dict


