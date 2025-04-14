
def count_words_in_book(book_text):
    word_list = book_text.split()
    return len(word_list)


def count_chars_in_book(book_text):
    char_count_dict = {}
    for i in book_text:
        if i.isalpha():
            char = i.lower()
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
    return char_count_dict


def sort_dict(char_dict):
    return char_dict["char_count"]


def dict_count_to_list(char_dict):
    list_of_char_dicts = []
    for k, v in char_dict.items():
        list_of_char_dicts.append({"char": k, "char_count": v})
    return list_of_char_dicts


def print_summary(path_to_book, word_count, sorted_list_of_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in sorted_list_of_dict:
        print(f"{d["char"]}: {d["char_count"]}")
    print("============= END =============== ")
