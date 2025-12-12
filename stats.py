def num_words(book_text):
    data_list = book_text.split()
    total_words = len(data_list)
    return f"Found {total_words} total words"

def count_chars(text):
    chars = {}
    lower_text = text.lower()

    for char in lower_text:
        if char not in chars:
            chars[char] = 1

        elif char in chars:
            chars[char] += 1

    return chars

def sort_dict(data):
    new_list = []
    for current_value in data:
        new_list.append({"char": current_value, "num": data[current_value]})

    def sort_on(items):
        return items["num"]
    
    new_list.sort(reverse=True, key=sort_on)
    return new_list

