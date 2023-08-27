import string

def censor_four_letter_words(input_filename, output_filename):
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            words = line.split()
            censored_words = []

            for word in words:
                # Remove punctuation from the word
                word = word.strip(string.punctuation)
                
                if len(word) == 4:
                    censored_words.append("****")
                else:
                    censored_words.append(word)
            
            censored_line = ' '.join(censored_words)
            output_file.write(censored_line + '\n')

def main():
    input_filename = input("Enter the input filename: ")
    output_filename = input("Enter the output filename: ")

    try:
        censor_four_letter_words(input_filename, output_filename)
        print("Censoring completed. Check the output file.")
    except FileNotFoundError:
        print("Input file not found.")

if __name__ == "__main__":
    main()
