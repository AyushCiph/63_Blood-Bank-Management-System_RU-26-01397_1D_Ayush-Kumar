# Blood Bank Management System

vg = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

stock = {
    "A+": 10,
    "A-": 0,
    "B+": 5,
    "B-": 0,
    "AB+": 2,
    "AB-": 0,
    "O+": 8,
    "O-": 0
}

# List to store donors
d = []


# Load donors from file
try:
    file = open("donors.txt", "r")

    for line in file:
        data = line.strip().split(",")

        if len(data) == 3:
            donor = {
                "name": data[0],
                "blood_group": data[1],
                "units": int(data[2])
            }

            d.append(donor)

    file.close()

except FileNotFoundError:
    pass


# Add donor
def add_donor():

    name = input("Enter donor name: ")
    blood_group = input("Enter blood group: ").upper()

    if blood_group not in vg:
        print("Invalid blood group. Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        return

    units = input("Enter units donated: ")

    if not units.isdigit() or int(units) <= 0:
        print("Units must be a positive whole number.")
        return

    units = int(units)

    donor = {
        "name": name,
        "blood_group": blood_group,
        "units": units
    }

    d.append(donor)

    # Save donor in file
    file = open("donors.txt", "a")
    file.write(name + "," + blood_group + "," + str(units) + "\n")
    file.close()

    # Add donated blood to stock
    stock[blood_group] = stock[blood_group] + units

    print("Donor saved to donors.txt.")
    print("Stock of", blood_group, "is now", stock[blood_group], "units.")


# Issue blood
def issue_blood():

    blood_group = input("Enter blood group: ").upper()

    if blood_group not in vg:
        print("Invalid blood group. Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        return

    units = input("Enter units required: ")

    if not units.isdigit() or int(units) <= 0:
        print("Units must be a positive whole number.")
        return

    units = int(units)

    if stock[blood_group] < units:
        print("Insufficient stock: only", stock[blood_group],
              "unit(s) of", blood_group, "available.")
        return

    stock[blood_group] = stock[blood_group] - units

    print(units, "unit(s) of", blood_group,
          "issued. Stock of", blood_group,
          "is now", stock[blood_group], "units.")


# View stock
def view_stock():

    print("\nBlood Stock:")

    for group in vg:
        print(group, ":", stock[group], "unit(s)")


# Search donors
def search_donors():

    blood_group = input("Enter blood group: ").upper()

    if blood_group not in vg:
        print("Invalid blood group. Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        return

    print("Donors with blood group", blood_group + ":")

    count = 0

    for donor in d:

        if donor["blood_group"] == blood_group:

            count = count + 1

            print(count, ".", donor["name"],
                  "-", donor["units"], "unit(s)")

    print("Total donors found:", count)


while True:

    print("\n===== BLOOD BANK MANAGEMENT SYSTEM =====")
    print("1. Add donor")
    print("2. Issue blood")
    print("3. View stock")
    print("4. Search donors")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_donor()

    elif choice == "2":
        issue_blood()

    elif choice == "3":
        view_stock()

    elif choice == "4":
        search_donors()

    elif choice == "5":
        print("Thank you for using Blood Bank Management System.")
        break

    else:
        print("Invalid choice. Please try again.")