def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_word_count(text)
    chars_dict = get_chars_dict(text)
    sorted_char_count_list = get_sorted_char_list(chars_dict)
    print_book_report(book_path, text, words, sorted_char_count_list)
    

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count(string):
    return len(string.split())

def get_chars_dict(string):
    chars_dict = {}
    lowercase_string = string.lower()
    for char in lowercase_string:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1

    return chars_dict

def sort_on(dict):
    return dict["num"]

def get_sorted_char_list(chars_dict):
    char_count_list = []
    for char in chars_dict:
        if char.isalpha():
            char_count_list.append({"name": char, "num": chars_dict[char]})
    char_count_list.sort(key=sort_on, reverse=True)
    return char_count_list


def print_book_report(book_path, book_text, word_count, chars_list):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    for char_item in chars_list:
        print(f"The '{char_item['name']}' character was found {char_item['num']} times")
    print("--- End report ---")

main()