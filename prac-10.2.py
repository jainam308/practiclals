def count_vowels_and_consonants(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

def main():
    input_string = input("Enter a string: ")
    vowel_count, consonant_count = count_vowels_and_consonants(input_string)
    
    print(f"Number of vowels: {vowel_count}")
    print(f"Number of consonants: {consonant_count}")

if __name__ == "__main__":
    main()
