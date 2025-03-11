import sys
import stats

def get_book_text(filepath):
    """Reads a file and returns its contents as a string."""
    try:
        with open(filepath) as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File not found at {filepath}"
    except Exception as e:
        return f"An error occurred: {e}"
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    
    """Reads and prints the contents of frankenstein.txt."""
    book_text = get_book_text(book_path)
    num_words = stats.count_words(book_text)
    num_chars = stats.count_characters(book_text)
    sorted_counts = stats.sort_char_counts(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_counts:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

main()