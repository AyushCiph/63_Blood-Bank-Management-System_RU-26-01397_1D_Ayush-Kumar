# 🩸 Blood Bank Management System

A beginner-friendly, menu-driven **Blood Bank Management System** developed using Python 3 as my first-semester college project.

This project helps manage blood donors, issue blood units, view available blood stock and search for donors based on their blood groups.

It uses basic Python concepts such as lists, dictionaries, functions, loops, conditional statements, file handling and Linear Search.

## 📌 Project Overview

| Detail | Description |
|---|---|
| Project Name | Blood Bank Management System |
| Project Number | 63 |
| Programming Language | Python 3 |
| Project Type | Console-Based Application |
| Data Storage | Text File (`donors.txt`) |
| Concepts Used | Lists, Dictionaries, Functions, Loops, File Handling and Searching |

## ✨ Features

- **Add Donor:** Register donors with their name, blood group and donated units.
- **Blood Group Validation:** Supports all eight standard blood groups.
- **Issue Blood:** Issue blood units according to available stock.
- **View Stock:** Display the available quantity of each blood group.
- **Search Donors:** Find registered donors by blood group using Linear Search.
- **File Handling:** Save donor records in `donors.txt`.
- **Input Validation:** Prevent invalid blood groups and non-positive or non-numeric unit inputs.
- **Stock Checking:** Prevent issuing more blood units than currently available.

## 🩸 Supported Blood Groups

The system supports eight blood groups:

- A+
- A-
- B+
- B-
- AB+
- AB-
- O+
- O-

## 📊 Initial Blood Stock

The program starts with the following predefined stock:

| Blood Group | Available Units |
|---|---:|
| A+ | 10 |
| A- | 0 |
| B+ | 5 |
| B- | 0 |
| AB+ | 2 |
| AB- | 0 |
| O+ | 8 |
| O- | 0 |

## 🛠️ Technologies and Concepts Used

**Technology:**
- Python 3

**Python Concepts:**
- Lists
- Dictionaries
- User-defined Functions
- `while` Loops
- `for` Loops
- Conditional Statements
- File Handling (`open()`, `read()`, `write()`)
- Exception Handling (`try-except`)
- Input Validation
- Linear Search

## 📂 Project Structure

```text
Blood-Bank-Management-System/
│
├── blood_bank.py
├── donors.txt
└── README.md
```

**Note:** The `donors.txt` file is automatically created when the first donor is registered. It stores donor information for future use.

## 🚀 How to Run the Project

**Step 1: Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2: Open the project folder**

```bash
cd Blood-Bank-Management-System
```

**Step 3: Run the Python program**

```bash
python blood_bank.py
```

**Step 4: Select an option from the menu.**

## 📋 Main Menu

```text
===== BLOOD BANK MANAGEMENT SYSTEM =====

1. Add donor
2. Issue blood
3. View stock
4. Search donors
5. Exit

Enter your choice:
```

## 💻 Sample Output

**Adding a donor:**

```text
Enter your choice: 1

Enter donor name: Rahul
Enter blood group: A+
Enter units donated: 2

Donor saved to donors.txt.
Stock of A+ is now 12 units.
```

**Viewing blood stock:**

```text
Blood Stock:

A+ : 12 unit(s)
A- : 0 unit(s)
B+ : 5 unit(s)
B- : 0 unit(s)
AB+ : 2 unit(s)
AB- : 0 unit(s)
O+ : 8 unit(s)
O- : 0 unit(s)
```

## 💾 Data Storage

The system uses a text file named `donors.txt` to store donor records.

Each record contains:

- Donor Name
- Blood Group
- Units Donated

**Example:**

```text
Rahul,A+,2
Amit,B+,3
Priya,O+,1
```

The program loads existing donor records when it starts and appends new donor records to the file.

**Note:** Blood stock is maintained using a Python dictionary. It returns to its predefined initial values whenever the program restarts. Blood donations and issues update the stock only during the current session.

## 📄 Project Documentation

The project report contains the introduction, objectives, features, Python concepts, program working, test cases and conclusion.

📖 **[View Project Documentation](https://docs.google.com/document/d/1keyCJgI8PNrFLvE-zpZRdb5-wkmTYicg_lbEjrE0ZQw/edit?usp=sharing)**

## 🎯 Learning Outcomes

Through this project, I practised:

- Using lists and dictionaries to manage data.
- Creating and using functions in Python.
- Reading and writing data using file handling.
- Creating a menu-driven application.
- Applying loops and conditional statements.
- Validating user inputs.
- Understanding Linear Search.
- Handling missing files using exception handling.

## 🔮 Future Improvements

- Save blood stock permanently using file handling or a database.
- Add donor registration IDs.
- Add blood compatibility information.
- Develop a graphical user interface.
- Generate blood donation and issue reports.
- Add an administrator login system.

## 👨‍💻 Author

**Ayush Kumar**

B.Tech CSE – Cyber Security  
Rungta International Skills University

Class: SA 04 | Section: 1D
