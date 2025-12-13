import sys
from stats import num_words, count_chars, sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("error please enter path to book")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    data = get_book_text(book)
    amount_words = num_words(data)
    chars = count_chars(data)
    print_loop = sort_dict(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------s")
    print(amount_words)
    print("--------- Character Count -------")

    for char in print_loop:
        print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")



main()