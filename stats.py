#function that takes string of word and returns the number of words
def word_count(book_words): 

    word_list = book_words.split()

    num_words = len(word_list)

    return num_words

#function that takes string of words and returns number of each character
def character_count(book_words): 

    count_dict = {}

    lower_letters = book_words.lower()

    for f in lower_letters:
            if f in count_dict:
                count_dict[f] += 1
            else:
                 count_dict[f] = 1

    return count_dict

#function to sort by with .sort
def sort_dict(dict):
     return dict["num"]

#function that takes dictionary of character and counts and returns sorted list of dictionaries
def list_dict(count_dict):
     
    d_list = []

    for c in count_dict:
          
        indi_dict = {"char": c, "num": count_dict[c]}
          
        d_list.append(indi_dict)
    

    d_list.sort(reverse=True, key=sort_dict)

    
    return d_list





        
    


