def convert_hex_to_decimal(hex_value):
    return int(hex_value, 16)

def main():
    hex_color = input("Enter a six-digit RGB color code (e.g., 00FF00): ")

    if len(hex_color) == 6 and all(c.isdigit() or ('A' <= c <= 'F') for c in hex_color.upper()):
        red = convert_hex_to_decimal(hex_color[0:2])
        green = convert_hex_to_decimal(hex_color[2:4])
        blue = convert_hex_to_decimal(hex_color[4:6])

        print(f"RGB Color Code: {hex_color}")
        print(f"Red: {red}")
        print(f"Green: {green}")
        print(f"Blue: {blue}")
    else:
        print("Invalid RGB color code. Please enter a six-digit hexadecimal value.")

if __name__ == "__main__":
    main()
