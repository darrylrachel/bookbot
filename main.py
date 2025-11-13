from stats import get_num_words, get_num_chars, sort_char_dict
import sys


def get_book_text(path: str):
    with open(path, 'r', encoding="utf-8") as f:
        return f.read()

# Checking if sys.argv has required entries

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book_path = sys.argv[1]
    book = get_book_text(book_path)



def main():
    word_result = get_num_words(book)
    char_counts = get_num_chars(book)
    sorted_chars = sort_char_dict(char_counts)

    print()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(word_result)
    print("--------- Character Count -------")

    # Print the sorted characters line-by-line
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    print()


main()
