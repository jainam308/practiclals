import string

def calculate_average_word_length(words):
    total_characters = sum(len(word.strip(string.punctuation)) for word in words)
    total_words = len(words)
    if total_words > 0:
        return total_characters / total_words
    else:
        return 0

def calculate_average_sentence_length(sentences):
    total_words = sum(len(sentence.split()) for sentence in sentences)
    total_sentences = len(sentences)
    if total_sentences > 0:
        return total_words / total_sentences
    else:
        return 0

def main():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()

            words = content.split()
            sentences = content.split('.')

            average_word_length = calculate_average_word_length(words)
            average_sentence_length = calculate_average_sentence_length(sentences)

            print(f"Average Word Length: {average_word_length:.2f}")
            print(f"Average Sentence Length: {average_sentence_length:.2f}")
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()
