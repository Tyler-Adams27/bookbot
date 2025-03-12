import sys

from stats import count_words
from stats import count_each_character
from stats import sort

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

frankenstein_text = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        book_content = f.read()
    return book_content

fin_dictionary = count_each_character(get_book_text(frankenstein_text))

def organise(fin_dictionary):
    for char, count in sort(fin_dictionary):
        if char.isalpha():
            print(f"{char}: {count}")


def main():
    print("============ BOOKBOT ============")







































    
    print(f"Analyzing book found at {frankenstein_text}...")
    print("----------- Word Count ---------")
    total_words = count_words(get_book_text(frankenstein_text))
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    organise(fin_dictionary)
    print("============= END ===============")

    

    


main()

