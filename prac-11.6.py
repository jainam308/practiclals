def remove_white_spaces(s):
    return s.replace(" ", "")

def interleave_strings(s1, s2):
    interleaved = ''.join([char1 + char2 for char1, char2 in zip(s1, s2)])
    if len(s1) > len(s2):
        interleaved += s1[len(s2):]
    elif len(s2) > len(s1):
        interleaved += s2[len(s1):]
    return interleaved

def main():
    try:
        with open("input1.txt", 'r') as file1, open("input2.txt", 'r') as file2:
            string1 = file1.read().strip()
            string2 = file2.read().strip()

            string1 = remove_white_spaces(string1)
            string2 = remove_white_spaces(string2)

            interleaved_string = interleave_strings(string1, string2)

            print("Interleaved String:", interleaved_string)
    except FileNotFoundError:
        print("Input files not found.")

if __name__ == "__main__":
    main()
