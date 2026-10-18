# Test Cases – Simulated Device Monitoring and Alert System

**Tested by:** Carl Moses K. Parungao
**Date of testing:** October 18, 2026

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 at startup | Five readings: 28, 31, 35, 37, 29 | [Pass] |
| TC02 | Choose 2, enter 33 | “Reading added successfully.” | [Pass] |
| TC03 | Choose 2, enter `abc` | Rejected; list unchanged | [Pass] |
| TC04 | Choose 2, enter `-5` | Rejected; list unchanged | [Pass] |
| TC05 | Choose 2, enter `120` | Rejected; list unchanged | [Pass] |
| TC06 | Add 30, then choose 3 | `30 °C -> WARNING` | [| TC08 | Choose 4 at startup | Total 160, average 32.00, min 28, max 37, status ATTENTION REQUIRED | [Pass] ]|
| TC07 | Choose 3 at startup | `35 °C -> WARNING` | [| TC08 | Choose 4 at startup | Total 160, average 32.00, min 28, max 37, status ATTENTION REQUIRED | [Pass] ]|
| TC08 | Choose 4 at startup | Total 160, average 32.00, min 28, max 37, status ATTENTION REQUIRED | [Pass] |
| TC09 | Enter menu choice `9` | Error message; menu shown again | [Pass] |
| TC10 | Choose 5 | Exit message; program ends | [Pass] |

## Additional Input Checks
- Empty reading: should be rejected with “Invalid input. The reading cannot be empty.”
- Decimal reading such as `3.5`: should be rejected with “Invalid input. Enter a whole number only.”
- Boundary range values `0` and `100`: should be accepted.
- Values `-1` and `101`: should be rejected.

## Bugs Found and Fixed
The classification function uses `reading < warning_limit` for NORMAL and `reading <= critical_limit` for WARNING. This makes both boundary values, 30 °C and 35 °C, WARNING. The minimum and maximum functions initialize from the first reading rather than zero, so the minimum is calculated correctly for the provided positive readings.
