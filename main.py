from stats import num_words, count_chars, sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    data = get_book_text("books/frankenstein.txt")
    amount_words = num_words(data)
    chars = count_chars(data)
    print(f"============ BOOKBOT ============")
    print(amount_words, "\n")
    print(sort_dict(chars))



main()