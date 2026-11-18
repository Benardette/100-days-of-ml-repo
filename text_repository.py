# Text Processing Functions

def clean_text(text):
    return text.strip()


def convert_to_lowercase(text):
    return text.lower()


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    return len(text)


def reverse_text(text):
    return text[::-1]


def main():
    text = input("Enter some text: ")

    print("\n--- Text Processing Results ---")
    print("Original text:", text)
    print("Cleaned text:", clean_text(text))
    print("Lowercase text:", convert_to_lowercase(text))
    print("Word count:", count_words(text))
    print("Character count:", count_characters(text))
    print("Reversed text:", reverse_text(text))

if __name__ == "__main__":
    main()
