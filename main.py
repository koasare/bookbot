# Write a new function called get_book_text. It takes a filepath as input and returns the contents of the file as a string.
def count_words(text):
    """Counts the number of words in a string."""
    words = text.split()
    return len(words)

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
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

main()