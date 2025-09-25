def get_num_words(book_text):
    words = book_text.split()
    return len(words)


def get_chars_dict(book_text):
    character_count = {}
    for character in book_text:
        c = character.lower()
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    return character_count


def sort_on(labeled_list):
    return labeled_list["num"]
    

def chars_dict_to_sorted_list(character_count):
    labeled_list = []
    for char, count in character_count.items():
        labeled_list.append({"char": char, "num": count})
    labeled_list.sort(key=sort_on, reverse=True)
    return labeled_list  # Return the list, don't print here
    