class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        self.average = self.calculate_average()

    def calculate_average(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student: {self.name}, Average: {self.average:.2f}"
        
class GradeManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, grades):
        student = Student(name, grades)
        self.students.append(student)

    def calculate_class_average(self):
        if not self.students:
            return 0
        total = sum(student.average for student in self.students)
        return total / len(self.students)

    def get_top_students(self):
        if not self.students:
            return []
        top_avg = max(student.average for student in self.students)
        top_students = [student for student in self.students if student.average == top_avg]
        return top_students

    def generate_report(self):
        report = []
        for student in self.students:
            report.append(f"{student.name}: {student.grades}, Average: {student.average:.2f}")
        return "\n".join(report)

def main():
    system = GradeManagementSystem()

    while True:
        print("\nStudent Grade Management System")
        print("1. Add Student Grades")
        print("2. View Class Average")
        print("3. View Top Performing Students")
        print("4. Generate Grade Report")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            grades_input = input("Enter student grades separated by spaces: ")
            grades = list(map(int, grades_input.split()))
            system.add_student(name, grades)
            print(f"{name}'s grades added successfully.")

        elif choice == '2':
            class_avg = system.calculate_class_average()
            print(f"Class Average: {class_avg:.2f}")

        elif choice == '3':
            top_students = system.get_top_students()
            print("Top Performing Student(s):")
            for student in top_students:
                print(student)

        elif choice == '4':
            print("\nGrade Report:")
            print(system.generate_report())

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()





