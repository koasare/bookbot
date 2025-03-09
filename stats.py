# Write a new function called get_book_text. It takes a filepath as input and returns the contents of the file as a string.
def count_words(text):
    """Counts the number of words in a string."""
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(unsorted_dict):
    sorted_char_counts = []
    for char, count in unsorted_dict.items():
        if char.isalpha():
            sorted_char_counts.append({"char": char, "count": count})
            sorted_char_counts.sort(key=lambda x: x["count"], reverse=True)
    return sorted_char_counts
