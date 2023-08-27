def create_file_with_string(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def read_entire_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        return content

def read_file_line_by_line(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        return lines

def write_string_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def write_list_to_file(file_name, lines_list):
    with open(file_name, 'w') as file:
        for line in lines_list:
            file.write(line + '\n')

def count_lines_words(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        
        word_count = 0
        for line in lines:
            words = line.split()
            word_count += len(words)
        
        return line_count, word_count

def main():
    file_name = "sample.txt"
    create_file_with_string(file_name, "Hello, this is a sample text.\nThis is the second line.")

    print("Reading entire file:")
    content = read_entire_file(file_name)
    print(content)
    
    print("\nReading file line by line:")
    lines = read_file_line_by_line(file_name)
    for line in lines:
        print(line.strip())
    
    append_content = "\nThis is an appended line."
    write_string_to_file(file_name, append_content)
    
    lines_list = ["Line 1", "Line 2", "Line 3"]
    write_list_to_file("output.txt", lines_list)
    
    line_count, word_count = count_lines_words(file_name)
    print(f"\nNumber of lines: {line_count}")
    print(f"Number of words: {word_count}")

if __name__ == "__main__":
    main()
