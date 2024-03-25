def main():
    book_path = "books/frankenstein.txt"
    book_report(book_path)

def book_report(book_path):
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_numbers = get_letter_counts(text)
    



def get_letter_counts(text):
    letter_counts = {}
    lower_text = text.lower()
    for letter in lower_text:
        if (letter.isalpha()):
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

# main execution
main()