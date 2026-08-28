
import os


# ==========================================================
# EXPENSE LIST
# ==========================================================

expensesList = []


# ==========================================================
# LOAD PREVIOUS EXPENSES FROM results.txt
# ==========================================================

if os.path.exists("results.txt"):

    with open("results.txt", "r", encoding="utf-8") as file:

        lines = file.readlines()

        date = None
        category = None
        description = None
        amount = None

        for line in lines:

            line = line.strip()

            if line.startswith("Date        :"):
                date = line.split(":", 1)[1].strip()

            elif line.startswith("Category    :"):
                category = line.split(":", 1)[1].strip()

            elif line.startswith("Description :"):
                description = line.split(":", 1)[1].strip()

            elif line.startswith("Amount      :"):

                try:
                    amount = float(line.split(":", 1)[1].strip())

                except ValueError:
                    amount = 0


                if (
                    date is not None
                    and category is not None
                    and description is not None
                ):

                    expensesList.append({
                        "date": date,
                        "category": category,
                        "description": description,
                        "amount": amount
                    })


                    date = None
                    category = None
                    description = None
                    amount = None


# ==========================================================
# WELCOME MESSAGE
# ==========================================================

print()
print("==================================================")
print("             WELCOME TO EXPENSE TRACKER")
print("==================================================")


# ==========================================================
# MAIN PROGRAM
# ==========================================================

while True:

    print()
    print("===================== MENU =======================")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expenses")
    print("4. Exit")
    print("==================================================")

    try:

        choice = int(input("Please enter your choice: "))

    except ValueError:

        print()
        print("Invalid input! Please enter a number from 1 to 4.")
        continue


    # ======================================================
    # 1. ADD EXPENSE
    # ======================================================

    if choice == 1:

        print()
        print("==================================================")
        print("                  ADD EXPENSE")
        print("==================================================")

        date = input("Enter expense date: ")

        category = input(
            "Enter expense category "
            "(Food, Travel, Smoke, Books/Notebook/Pen, Extra): "
        )

        description = input("Enter expense description: ")


        try:

            amount = float(input("Enter expense amount: "))

        except ValueError:

            print()
            print("Invalid amount! Please enter a number.")
            continue


        # Create expense

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }


        # Add expense to list

        expensesList.append(expense)


        # ==================================================
        # SAVE ADD EXPENSE TO results.txt
        # ==================================================

        expense_number = len(expensesList)

        with open("results.txt", "a", encoding="utf-8") as file:

            file.write("\n")
            file.write("==================================================\n")
            file.write(f"                  EXPENSE #{expense_number}\n")
            file.write("==================================================\n")
            file.write(f"Date        : {date}\n")
            file.write(f"Category    : {category}\n")
            file.write(f"Description : {description}\n")
            file.write(f"Amount      : {amount:.2f}\n")
            file.write("==================================================\n")


        print()
        print("Expense added successfully!")
        print("Data saved to results.txt.")


    # ======================================================
    # 2. VIEW ALL EXPENSES
    # ======================================================

    elif choice == 2:

        if len(expensesList) == 0:

            print()
            print("No expenses found.")

        else:

            print()
            print("==================================================")
            print("                 ALL EXPENSES")
            print("==================================================")


            # ----------------------------------------------
            # SHOW IN TERMINAL
            # ----------------------------------------------

            count = 1

            for eachExpense in expensesList:

                print()
                print("--------------------------------------------------")
                print(f"                  EXPENSE #{count}")
                print("--------------------------------------------------")

                print(f"Date        : {eachExpense['date']}")
                print(f"Category    : {eachExpense['category']}")
                print(f"Description : {eachExpense['description']}")
                print(f"Amount      : {eachExpense['amount']:.2f}")

                print("--------------------------------------------------")

                count += 1


            print()
            print("==================================================")


            # ----------------------------------------------
            # SAVE VIEW RESULT TO results.txt
            # ----------------------------------------------

            with open("results.txt", "a", encoding="utf-8") as file:

                file.write("\n")
                file.write("\n")
                file.write("##################################################\n")
                file.write("                 ALL EXPENSES\n")
                file.write("##################################################\n")


                count = 1

                for eachExpense in expensesList:

                    file.write("\n")
                    file.write("--------------------------------------------------\n")
                    file.write(f"                  EXPENSE #{count}\n")
                    file.write("--------------------------------------------------\n")
                    file.write(
                        f"Date        : {eachExpense['date']}\n"
                    )
                    file.write(
                        f"Category    : {eachExpense['category']}\n"
                    )
                    file.write(
                        f"Description : {eachExpense['description']}\n"
                    )
                    file.write(
                        f"Amount      : {eachExpense['amount']:.2f}\n"
                    )
                    file.write("--------------------------------------------------\n")

                    count += 1


                file.write("##################################################\n")


            print("View result saved to results.txt.")


    # ======================================================
    # 3. VIEW TOTAL EXPENSES
    # ======================================================

    elif choice == 3:

        total = 0


        for eachExpense in expensesList:

            total = total + eachExpense["amount"]


        # ----------------------------------------------
        # SHOW TOTAL IN TERMINAL
        # ----------------------------------------------

        print()
        print("==================================================")
        print("                 EXPENSE SUMMARY")
        print("==================================================")
        print(f"Number of Expenses : {len(expensesList)}")
        print(f"Total Expenses     : {total:.2f}")
        print("==================================================")


        # ----------------------------------------------
        # SAVE TOTAL RESULT TO results.txt
        # ----------------------------------------------

        with open("results.txt", "a", encoding="utf-8") as file:

            file.write("\n")
            file.write("\n")
            file.write("##################################################\n")
            file.write("                 EXPENSE SUMMARY\n")
            file.write("##################################################\n")
            file.write(
                f"Number of Expenses : {len(expensesList)}\n"
            )
            file.write(
                f"Total Expenses     : {total:.2f}\n"
            )
            file.write("##################################################\n")


        print("Summary saved to results.txt.")


    # ======================================================
    # 4. EXIT
    # ======================================================

    elif choice == 4:

        print()
        print("==================================================")
        print("       Thanks for using the Expense Tracker!")
        print("==================================================")

        break


    # ======================================================
    # INVALID CHOICE
    # ======================================================

    else:

        print()
        print("Invalid choice!")
        print("Please enter a number between 1 and 4.")