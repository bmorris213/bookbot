def main():
    book_path = "books/frankenstein.txt"
    book_report(book_path)

def book_report(book_path):
    print (f"--- Begin report of {book_path} ---")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_numbers = get_letter_counts(text)
    print (f"{num_words} words found in the document.")
    for letter in letter_numbers:
        print (f"The '{letter}' character was found {letter_numbers[letter]} times.")
    print ("--- End report ---")


def get_letter_counts(text):
    letter_counts = {}
    lower_text = text.lower()
    for letter in lower_text:
        if (letter.isalpha()):
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return dict(sorted(letter_counts.items(), key=lambda x: x[1], reverse=True))

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

# main execution
main()