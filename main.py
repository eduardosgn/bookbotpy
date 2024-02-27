def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_letters(text):
    counts = {}
    for char in text.lower():
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

def get_num_words(text):
    words = text.split()
    return len(words)
    
def sort_counts(counts):
    counts_list = []
    for letter, count in counts.items():
        item_dict = {"letter": letter, "count": count}
        counts_list.append(item_dict)
    counts_list.sort(key=lambda x: x["letter"], reverse=False)
    return counts_list
    
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = count_letters(text)
    sorted_letter_counts = sort_counts(letter_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for letter_count in sorted_letter_counts:
        print(f"The '{letter_count['letter']}' character was found {letter_count['count']} times")

    print("--- End report ---")

main()