def main():
    state_capitals = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        # Add more states and capitals here
    }

    while True:
        state = input("Enter a state (or 'exit' to quit): ").strip().title()

        if state == 'Exit':
            print("Exiting the program.")
            break

        if state in state_capitals:
            correct_capital = state_capitals[state]
            user_input = input(f"What is the capital of {state}? ").strip().title()

            if user_input == correct_capital:
                print("Correct!")
            else:
                print(f"Sorry, the correct capital of {state} is {correct_capital}.")
        else:
            print("State not found in the dictionary. Please enter a valid state.")

if __name__ == "__main__":
    main()
