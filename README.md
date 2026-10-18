# Simulated Device Monitoring and Alert System

**Student Name:** Carl Moses K. Parungao 
**Student Number: 2601356
**Section:** 1CPE-B

## 1. Project Description
This Python program simulates a device-temperature monitoring system for a Computer Engineering laboratory. It stores temperature readings, classifies them as NORMAL, WARNING, or CRITICAL, and generates a summary of the readings. The program is a classroom simulation only and does not connect to real sensors or determine actual device safety.

## 2. Features
- View all stored temperature readings with their positions.
- Add whole-number readings from 0 to 100 inclusive.
- Reject empty, non-numeric, negative, and above-range input.
- Classify readings using the required temperature rules.
- Calculate the total, average, minimum, maximum, category counts, percentages, and overall status.
- Repeat the menu until Exit is selected.

## 3. Requirements
- Python 3
- No external packages are required.

## 4. How to Run
1. Open a terminal in the `Week17` folder.
2. Run `python device_monitor.py`.
3. On systems where Python 3 uses a separate command, run `python3 device_monitor.py`.

## 5. Sample Output
The following summary is expected when the program is started and option 4 is selected before adding any readings:

```text
MONITORING SUMMARY
------------------
Number of readings : 5
Total of readings   : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL   : 2 (40.00%)
WARNING  : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED
```

## 6. Test Cases
Ten required tests are listed in [`test_cases.md`](test_cases.md). Run the tests in your local Python environment and update the Actual Result and Pass/Fail columns to match what you observe.

## 7. Known Limitations
- Readings are stored in memory and are lost when the program closes.
- Readings are simulated; the program does not connect to a physical device or sensor.
- The thresholds are for this classroom exercise and are not real device-safety standards.

## 8. Reflection
This project combines lists, loops, selection statements, functions, parameters, return values, and input validation in one program. A key challenge is checking input before converting it to an integer so invalid values do not enter the list. Boundary values are handled using inclusive comparisons so that 30 °C and 35 °C are both WARNING. The project could be improved in the future by saving readings between sessions or connecting to a real sensor, if those features were allowed.

## 9. Classification Rules
- Below 30 °C: NORMAL
- 30 °C to 35 °C inclusive: WARNING
- Above 35 °C: CRITICAL

## 10. Input Validation
The program rejects empty input, non-integer text such as `abc` or `3.5`, and integer readings outside 0–100. Invalid readings are not appended to the list. Invalid menu choices display an error and return to the menu.

## 11. Numerical Processing
The program uses loops to calculate the total, minimum, maximum, and category counts. The average is calculated by dividing the total by the number of readings. Category percentages are calculated as `count / number_of_readings * 100`. The program does not use `sum()`, `min()`, or `max()`.

## 12. Functions and Program Structure
- `get_initial_readings()` returns the initial list.
- `is_whole_number(text)` checks the input format.
- `add_reading(readings, text, lowest, highest)` validates and adds a reading.
- `classify_reading(reading, warning_limit, critical_limit)` returns a category.
- `compute_total()`, `compute_average()`, `find_minimum()`, and `find_maximum()` calculate numerical results.
- `count_category()` counts a requested category.
- `determine_overall_status()` returns the overall status.
- Display functions show readings, classifications, the summary, and the menu.
- `main()` controls the menu loop and calls the other functions.
