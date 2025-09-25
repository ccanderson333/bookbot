from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    book_text = content
    return book_text

def print_report(file_path, word_count, sorted_character_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in sorted_character_list:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item["num"]}")

    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    word_count = get_num_words(book_text)
    character_count = get_chars_dict(book_text)
    sorted_character_list = chars_dict_to_sorted_list(character_count)

    print_report(file_path, word_count, sorted_character_list)

main()

