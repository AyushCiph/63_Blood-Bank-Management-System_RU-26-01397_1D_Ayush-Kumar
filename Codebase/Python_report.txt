Blood Bank Management System

Python Project – Problem Statement No. 63

Submitted By: Ayush Kumar
Class: SA 04
Section: D1
ERP: RU-26-01397

---

1. Introduction

The Blood Bank Management System is a console-based Python project developed to manage blood donors and blood stock. It allows staff to add donor details, issue blood, check available stock, and search for donors based on their blood groups.

The main purpose of this project is to make basic blood bank operations easier and maintain accurate blood stock records.

2. Problem Statement

Blood bank staff need a simple system to manage donors and blood availability. Maintaining records manually can make it difficult to track available units and find donors when required.

This project provides a simple solution using Python. It stores blood stock in a dictionary, donor information in a list, and saves donor records permanently in a text file named "donors.txt".

3. Objectives

The main objectives of this project are:

- To add and store donor information.
- To maintain blood stock for all valid blood groups.
- To issue blood only when sufficient units are available.
- To search for donors according to their blood groups.
- To save donor records using file handling.
- To prevent invalid blood groups and incorrect unit entries.

4. Technologies and Concepts Used

Programming Language: Python 3

The following Python concepts are used:

Concept| Purpose
Dictionary| Stores blood stock for each blood group.
List| Maintains donor records.
File Handling| Saves and loads donor information.
Loops| Displays the menu repeatedly.
Conditional Statements| Handles menu options and validations.
Functions| Organizes different operations of the program.
Searching| Finds donors based on blood groups.

5. System Requirements

Software Requirements:

- Python 3
- Visual Studio Code or any Python-supported editor
- Command Prompt or Terminal

Valid Blood Groups:

A+, A-, B+, B-, AB+, AB-, O+, O-

Initial Blood Stock:

Blood Group| Available Units
A+| 10
A-| 0
B+| 5
B-| 0
AB+| 2
AB-| 0
O+| 8
O-| 0

The "donors.txt" file initially contains two donor records:

1. Meena Joshi – O+ – 1 unit
2. Suresh Rao – O+ – 2 units

6. Features of the Project

The program provides five main menu options:

1. Add Donor

Allows the user to enter a donor's name, blood group, and number of units. The information is stored in the donor list and saved in "donors.txt". The corresponding blood stock is also updated.

2. Issue Blood

Allows the user to issue blood according to the required blood group and units. The program checks the available stock before issuing blood. If sufficient units are not available, the request is rejected.

3. View Stock

Displays all eight blood groups along with their currently available units.

4. Search Donors

Searches for donors using their blood groups and displays matching donor details along with the total number of matching records.

5. Exit

Closes the program.

7. Program Design and Working

The program starts by loading the existing donor records from "donors.txt".

After loading the records, a menu is displayed. The user can select an operation by entering the corresponding menu number.

The program continues running until the user selects the Exit option.

The main working process is:

1. Load donor records from the text file.
2. Display the main menu.
3. Accept the user's choice.
4. Perform the selected operation.
5. Validate the entered information.
6. Update the donor records or blood stock when required.
7. Return to the main menu.

This process helps maintain donor information and blood stock during program execution.

8. Testing

The following test cases are based on the project requirements.

Test Case| Input| Expected Result
Normal Input| Add Ani Verma, B+, 1 unit| Donor saved and B+ stock becomes 6.
Minimum Stock| Issue AB+, 2 units| 2 units issued and AB+ stock becomes 0.
Invalid Stock| Issue A-, 3 units| Request rejected because no units are available.
Invalid Blood Group| Add Rina Das, C+, 1 unit| Request rejected because C+ is not valid.
Donor Search| Search for O+| Meena Joshi and Suresh Rao are displayed.

Testing Status: Update the results after running each test case in the program.

9. Limitations

Although the program performs basic blood bank operations, it has some limitations:

- It is designed for a single-user environment.
- It does not have a login or authentication system.
- Donor information is stored in a text file.
- It does not maintain donation dates.
- It does not check donor eligibility.

10. Future Improvements

The project can be improved by adding:

- A login system for authorized staff.
- Database integration for better data management.
- Automatic low-stock alerts.
- Donation date tracking.
- Donor eligibility checking.
- A graphical user interface for easier operation.

11. Conclusion

The Blood Bank Management System successfully demonstrates the use of basic Python programming concepts in a practical project.

It uses dictionaries to manage blood stock, lists to maintain donor records, and file handling to save information permanently. It also includes validation to prevent invalid entries and issuing more blood than the available stock.

Through this project, I gained practical experience in Python programming, data structures, file handling, loops, and conditional statements.

---

Project: Blood Bank Management System
Problem Statement: PS No. 63
Language: Python 3
Submitted by: Ayush Kumar