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
    """Reads and prints the contents of frankenstein.txt."""
    book_text = get_book_text("books/frankenstein.txt")
    num_words = stats.count_words(book_text)
    num_chars = stats.count_characters(book_text)
    sorted_counts = stats.sort_char_counts(num_chars)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_counts:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

main()