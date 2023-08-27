def find_days_in_temperature_range(temperature_dict, min_temp, max_temp):
    days_in_range = []
    for day, temp in temperature_dict.items():
        if min_temp <= temp <= max_temp:
            days_in_range.append(day)
    return days_in_range

def main():
    temperature_dict = {
        "Monday": 45,
        "Tuesday": 38,
        "Wednesday": 48,
        "Thursday": 50,
        "Friday": 42,
        "Saturday": 39,
        "Sunday": 52
    }

    min_temp = 40
    max_temp = 50

    days_in_range = find_days_in_temperature_range(temperature_dict, min_temp, max_temp)

    if days_in_range:
        print(f"Days with average temperature between {min_temp} and {max_temp} degrees:")
        print(", ".join(days_in_range))
    else:
        print(f"No days found with average temperature between {min_temp} and {max_temp} degrees.")

if __name__ == "__main__":
    main()
