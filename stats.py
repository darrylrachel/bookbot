def get_num_words(text: str) -> str:
    words = text.split()
    return f"Found {len(words)} total words"


def get_num_chars(text: str) -> dict:
    counts = {}

    for char in text.lower():
        if char.isalpha(): # ONLY alphabetical chars
            counts[char] = counts.get(char, 0) + 1

    return counts


# NEW! Boot.dev-required function
def sort_char_dict(counts: dict) -> list[dict]:
    # Turn the character-count dict into a list of dicts
    char_list = [{"char": char, "num": count} for char, count in counts.items()]

    # Sort in-place using .sort()
    # key helper = sort by "num" in descending order
    char_list.sort(key=lambda item: item["num"], reverse=True)

    return char_list


#print(f"Sys Argv: {sys.argv}") # prints root
#print(f"Sys Argv0: {sys.argv[0]}") # prints main.py
#print(f"Sys Argv1: {sys.argv[1]}") # prints books/frankenstein.txt

# book = sys.argv

# def get_book_path(book = sys.argv):
#     if len(book) != 2:
#         print("Usage: python3 main.py <path_to_book>")
#         print(sys.exit(1))
#     else:
#         print(book)
# get_book_path()

