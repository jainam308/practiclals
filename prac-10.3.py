def convert_date_format(date_str):
    # Split the input date string into day, month, and year
    day, month, year = date_str.split('/')
    
    # Reformat the date string into MM-DD-YYYY format
    new_date_str = f"{month}-{day}-{year}"
    
    return new_date_str

def main():
    date_input = input("Enter a date in the format DD/MM/YYYY: ")
    
    try:
        converted_date = convert_date_format(date_input)
        print("Date in MM-DD-YYYY format:", converted_date)
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY.")

if __name__ == "__main__":
    main()
