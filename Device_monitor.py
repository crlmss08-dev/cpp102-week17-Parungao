def get_initial_readings():
    """Return the required starting temperature readings."""
    return [28, 31, 35, 37, 29]


def is_whole_number(text):
    """Return True when text contains an optional leading minus and digits only."""
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":
        start = 1
    if start == len(text):
        return False
    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False
    return True


def add_reading(readings, text, lowest, highest):
    """Validate text and append a reading only when it is a whole number in range."""
    if len(text) == 0:
        print("Invalid input. The reading cannot be empty.")
        return False
    if not is_whole_number(text):
        print("Invalid input. Enter a whole number only.")
        return False

    reading = int(text)
    if reading < lowest or reading > highest:
        print(f"Invalid reading. Enter a value from {lowest} to {highest}.")
        return False

    readings.append(reading)
    print("Reading added successfully.")
    return True


def classify_reading(reading, warning_limit, critical_limit):
    """Return NORMAL, WARNING, or CRITICAL for one temperature reading."""
    if reading < warning_limit:
        return "NORMAL"
    elif reading <= critical_limit:
        return "WARNING"
    else:
        return "CRITICAL"


def compute_total(readings):
    """Return the total of all readings using a loop."""
    total = 0
    for reading in readings:
        total = total + reading
    return total


def compute_average(readings):
    """Return the average of the readings."""
    return compute_total(readings) / len(readings)


def find_minimum(readings):
    """Return the smallest reading using a loop."""
    minimum = readings[0]
    for reading in readings:
        if reading < minimum:
            minimum = reading
    return minimum


def find_maximum(readings):
    """Return the largest reading using a loop."""
    maximum = readings[0]
    for reading in readings:
        if reading > maximum:
            maximum = reading
    return maximum


def count_category(readings, warning_limit, critical_limit, category):
    """Count readings that match the requested classification."""
    count = 0
    for reading in readings:
        if classify_reading(reading, warning_limit, critical_limit) == category:
            count = count + 1
    return count


def determine_overall_status(warning_count, critical_count):
    """Return the overall monitoring status from the category counts."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_readings(readings):
    """Display each stored reading with its position."""
    print("\nCURRENT READINGS")
    print("----------------")
    for index in range(len(readings)):
        print(f"Reading {index + 1}: {readings[index]} °C")


def display_classifications(readings, warning_limit, critical_limit):
    """Display the classification of every stored reading."""
    print("\nREADING CLASSIFICATION")
    print("----------------------")
    for reading in readings:
        category = classify_reading(reading, warning_limit, critical_limit)
        print(f"{reading} °C -> {category}")


def display_summary(readings, warning_limit, critical_limit):
    """Calculate and display numerical statistics and overall status."""
    total = compute_total(readings)
    number_of_readings = len(readings)
    average = total / number_of_readings
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)

    normal_count = count_category(readings, warning_limit, critical_limit, "NORMAL")
    warning_count = count_category(readings, warning_limit, critical_limit, "WARNING")
    critical_count = count_category(readings, warning_limit, critical_limit, "CRITICAL")

    normal_percentage = normal_count / number_of_readings * 100
    warning_percentage = warning_count / number_of_readings * 100
    critical_percentage = critical_count / number_of_readings * 100
    overall_status = determine_overall_status(warning_count, critical_count)

    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings : {number_of_readings}")
    print(f"Total of readings   : {total}")
    print(f"Average temperature : {average:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")
    print()
    print(f"NORMAL   : {normal_count} ({normal_percentage:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_percentage:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_percentage:.2f}%)")
    print()
    print(f"Overall Status: {overall_status}")


def display_menu():
    """Display the main menu options."""
    print("\nSIMULATED DEVICE MONITORING SYSTEM")
    print("----------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def main():
    """Run the menu loop and connect the monitoring functions."""
    readings = get_initial_readings()
    warning_limit = 30
    critical_limit = 35

    while True:
        display_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            text = input("Enter new reading: ")
            add_reading(readings, text, 0, 100)
        elif choice == "3":
            display_classifications(readings, warning_limit, critical_limit)
        elif choice == "4":
            display_summary(readings, warning_limit, critical_limit)
        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
