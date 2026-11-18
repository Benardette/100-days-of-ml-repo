#Study Tracker
 # 1. DATA TYPES
study_sessions = [2, 5, 3, 4, 1, 3, 4, 5, 2]       # List
daily_goal = 4.0         # Float

# 2. WELCOME MESSAGE
print("===================================")
print("       MY STUDY HOURS TRACKER")
print("===================================")

while True:

    print("\nMAIN MENU")
    print("1. Add study session")
    print("2. View study records")
    print("3. View total study hours")
    print("4. Check daily goal")
    print("5. Exit")

    choice = input("\nChoose an option (1-5): ")
  # ADD STUDY SESSION
    if choice == "1":

        subject = "Python Basics"
        date = " 2nd Nov 2026: "

        try:
            hours = 6

            if hours <= 0:
                print("Please enter hours greater than zero.")

            else:
                session = {
                    "subject": subject,
                    "date": date,
                    "hours": hours
                }

                study_sessions.append(session)

                print("\nStudy session added successfully!")

        except ValueError:
            print("Invalid hours. Enter a number.")

    # VIEW STUDY HISTORY
    elif choice == "2":

        if not study_sessions:
            print("No study sessions recorded yet.")

        else:
            print("\n======= STUDY HISTORY =======")

            for session in study_sessions:
                print(f"Date: {session['date']}")
                print(f"Subject: {session['subject']}")
                print(f"Hours: {session['hours']}")
                print("-----------------------------")

    # TOTAL STUDY HOURS
    elif choice == "3":

        total = sum(session["hours"] for session in study_sessions)

        print(f"\nTotal hours studied: {total:.2f}")

    # SUBJECT STATISTICS
    elif choice == "4":

        if not study_sessions:
            print("No data available.")

        else:
            subject_totals = {}

            for session in study_sessions:
                subject = session["subject"]
                hours = session["hours"]

                if subject in subject_totals:
                    subject_totals[subject] += hours
                else:
                    subject_totals[subject] = hours

            print("\n======= SUBJECT STATISTICS =======")

            for subject, hours in subject_totals.items():
                print(f"{subject}: {hours} hours")

    # CHECK STUDY GOAL
    elif choice == "5":

        total = sum(session["hours"] for session in study_sessions)

        print(f"\nDaily goal: {daily_goal} hours")
        print(f"Hours recorded: {total} hours")

        if total >= daily_goal:
            print("Excellent! Study goal achieved.")

        else:
            remaining = daily_goal - total
            print(f"You need {remaining:.2f} more hours.")

    # EXIT
    elif choice == "6":

        print("Keep learning. Keep improving!")
        break

    else:
        print("Invalid option. Try again.")
