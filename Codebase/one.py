
# Blood Bank Management System

blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

# Initial blood stock
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

# List to store donor details
donors = []


try:
    donor_file = open("donors.txt", "r")

    for line in donor_file:

        donor_data = line.strip().split(",")

        if len(donor_data) == 3:

            donor_name = donor_data[0]
            donor_blood_group = donor_data[1]
            donated_units = int(donor_data[2])

            donor_details = {
                "name": donor_name,
                "blood_group": donor_blood_group,
                "units": donated_units
            }

            donors.append(donor_details)

    donor_file.close()

except FileNotFoundError:
    pass


# add a new donor
def add_donor():

    donor_name = input("Enter donor name: ")
    donor_blood_group = input("Enter blood group: ").upper()

    if donor_blood_group not in blood_groups:

        print("Invalid blood group. Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        return

    donated_units = input("Enter units donated: ")

    if not donated_units.isdigit() or int(donated_units) <= 0:

        print("Units must be a positive whole number.")
        return

    donated_units = int(donated_units)

    donor_details = {
        "name": donor_name,
        "blood_group": donor_blood_group,
        "units": donated_units
    }

    donors.append(donor_details)

    # Save donor details in file
    donor_file = open("donors.txt", "a")

    donor_file.write(
        donor_name + "," +
        donor_blood_group + "," +
        str(donated_units) + "\n"
    )

    donor_file.close()

    # Update blood stock
    current_stock = stock[donor_blood_group]
    updated_stock = current_stock + donated_units

    stock[donor_blood_group] = updated_stock

    print("Donor saved to donors.txt.")
    print("Stock of", donor_blood_group, "is now", updated_stock, "units.")


# issue blood
def issue_blood():

    requested_blood_group = input("Enter blood group: ").upper()

    if requested_blood_group not in blood_groups:

        print("Invalid blood group. Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        return

    required_units = input("Enter units required: ")

    if not required_units.isdigit() or int(required_units) <= 0:

        print("Units must be a positive whole number.")
        return

    required_units = int(required_units)

    available_units = stock[requested_blood_group]

    if available_units < required_units:

        print("Insufficient stock: only", available_units,
              "unit(s) of", requested_blood_group, "available.")
        return

    remaining_units = available_units - required_units

    stock[requested_blood_group] = remaining_units

    print(required_units, "unit(s) of", requested_blood_group,
          "issued. Stock of", requested_blood_group,
          "is now", remaining_units, "units.")


# display blood stock
def view_stock():

    print("\nBlood Stock:")

    for blood_group in blood_groups:

        available_units = stock[blood_group]

        print(blood_group, ":", available_units, "unit(s)")


# search donors
def search_donors():

    search_blood_group = input("Enter blood group: ").upper()

    if search_blood_group not in blood_groups:

        print("Invalid blood group. Valid groups: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        return

    print("Donors with blood group", search_blood_group + ":")

    donor_count = 0

    for donor_details in donors:

        if donor_details["blood_group"] == search_blood_group:

            donor_count = donor_count + 1

            donor_name = donor_details["name"]
            donated_units = donor_details["units"]

            print(donor_count, ".", donor_name,
                  "-", donated_units, "unit(s)")

    print("Total donors found:", donor_count)


# Main menu
while True:

    print("\n===== BLOOD BANK MANAGEMENT SYSTEM =====")
    print("1. Add donor")
    print("2. Issue blood")
    print("3. View stock")
    print("4. Search donors")
    print("5. Exit")

    user_choice = input("Enter your choice: ")

    if user_choice == "1":

        add_donor()

    elif user_choice == "2":

        issue_blood()

    elif user_choice == "3":

        view_stock()

    elif user_choice == "4":

        search_donors()

    elif user_choice == "5":

        print("Thank you for using Blood Bank Management System.")
        break

    else:

        print("Invalid choice. Please try again.")
