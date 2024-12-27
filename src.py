
def add_grade(grades, grade):
    grades.append(grade)
    print(f"Grade {grade} added successfully.")

def view_grades(grades):
    if not grades:
        print("No grades available.")
    else:
        for i, grade in enumerate(grades, start=1):
            print(f"Grade {i}: {grade}")

def calculate_average(grades):
    if not grades:
        print("No grades available to calculate the average.")
    else:
        average = sum(grades) / len(grades)
        print(f"The average grade is: {average:.2f}")

def find_highest_grade(grades):
    if not grades:
        print("No grades available to find the highest grade.")
    else:
        highest = max(grades)
        print(f"The highest grade is: {highest}")

def find_lowest_grade(grades):
    if not grades:
        print("No grades available to find the lowest grade.")
    else:
        lowest = min(grades)
        print(f"The lowest grade is: {lowest}")

def get_choice():
    print("\nStudent Grades Management System")
    print("1. Add Grade")
    print("2. View Grades")
    print("3. Calculate Average Grade")
    print("4. Find Highest Grade")
    print("5. Find Lowest Grade")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")
    return choice

def main():
    grades = []

    while True:
        choice = get_choice()

        if choice == '6':
            print("Exiting the system. Goodbye!")
            break

        if choice == '1':
            grade = float(input("Enter the grade: "))
            add_grade(grades, grade)
        elif choice == '2':
            view_grades(grades)
        elif choice == '3':
            calculate_average(grades)
        elif choice == '4':
            find_highest_grade(grades)
        elif choice == '5':
            find_lowest_grade(grades)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





