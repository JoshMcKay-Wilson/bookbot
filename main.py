import sys
from stats import count_words_in_book, count_chars_in_book, sort_dict, dict_count_to_list, print_summary

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    

def main():  

    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    path_to_frankenstein = sys.argv[1]
    frankenstein_text = get_book_text(path_to_frankenstein)
    num_words = count_words_in_book(frankenstein_text)

    #print(f"{num_words} words found in the document")
    char_count_dict = count_chars_in_book(frankenstein_text)

    list_of_char_counts = dict_count_to_list(char_count_dict)
    list_of_char_counts.sort(reverse=True, key=sort_dict)
    #print(list_of_char_counts)

    print_summary(path_to_frankenstein, num_words, list_of_char_counts)

main()