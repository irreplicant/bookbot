from stats import get_word_count
from stats import get_letter_counts
from stats import sort_letters
import sys

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(filename, word_count, letter_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for d in letter_counts:
        c = d["char"]
        n = d["num"]
        print(f"{c}: {n}")


def main():
    if(len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    contents = get_book_text(path)
    num_words = get_word_count(contents)
    letter_counts = get_letter_counts(contents)
    sorted_letters = sort_letters(letter_counts)

    print_report(path, num_words, sorted_letters)

main()


