"""
COMP.CS.100 Programming 1
A Program that reads course data from a file and builds a
nested dictionary of the departments and courses.

Author:Ifeoma Nwankwo
Student Number: 152577546
Email: ifeoma.nwankwo@tuni.fi
"""
def read_courses_from_file(filename):
    """
    Reads course data from a file and builds a nested dictionary of departments and courses.

    The file should have lines in the format:
        department;course_name;credits
    Each course belongs to a department and has integer credits.

    Args:
        filename (str): Path to the input file containing course data.

    Returns:
        dict or None: A dictionary where keys are department names, and values are dictionaries
                      of course names to credits. Returns None if file cannot be opened or format is wrong.
    """
    departments = {}
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(";")
                if len(parts) != 3:
                    print("Error in file!")
                    return None
                department, course_name, credit_str = parts
                try:
                    credits = int(credit_str)
                except ValueError:
                    print("Error in file!")
                    return None

                if department not in departments:
                    departments[department] = {}
                departments[department][course_name] = credits
        return departments
    except FileNotFoundError:
        print("Error opening file!")
        return None


def print_all(departments):
    """
    Prints all departments and their courses with credits in alphabetical order.

    Args:
        departments (dict): Dictionary of departments and their courses.
    """
    for dept in sorted(departments.keys()):
        print(f"*{dept}*")
        for course in sorted(departments[dept].keys()):
            print(f"{course} : {departments[dept][course]} cr")


def print_department(departments, department):
    """
    Prints all courses and their credits of a single department.

    Args:
        departments (dict): Dictionary of departments and courses.
        department (str): The department name to print.
    """
    if department not in departments:
        print("Department not found!")
        return
    print(f"*{department}*")
    for course in sorted(departments[department].keys()):
        print(f"{course} : {departments[department][course]} cr")


def credits_of_department(departments, department):
    """
    Prints the total credits offered by the specified department.

    Args:
        departments (dict): Dictionary of departments and courses.
        department (str): The department to calculate total credits for.
    """
    if department not in departments:
        print("Department not found!")
        return
    total_credits = sum(departments[department].values())
    print(f"Department {department} has to offer {total_credits} cr.")


def add_course(departments, command_args):
    """
    Adds a new course to a department or creates a new department with the course.

    Args:
        departments (dict): Dictionary of departments and courses.
        command_args (list): List of strings containing department, course name (possibly multiple words), and credits.
                             Format: [department, course_name..., credits]
    """
    if len(command_args) < 3:
        print("Invalid command!")
        return

    department = command_args[0]
    try:
        credits = int(command_args[-1])
    except ValueError:
        print("Invalid command!")
        return

    course_name = " ".join(command_args[1:-1])

    if department not in departments:
        departments[department] = {course_name: credits}
        print(f"Added department {department} with course {course_name}")
    else:
        if course_name in departments[department]:
            # Overwrite existing course credits if course exists
            departments[department][course_name] = credits
        else:
            departments[department][course_name] = credits
        print(f"Added course {course_name} to department {department}")


def delete_command(departments, command_args):
    """
    Deletes a department or a specific course from a department.

    Args:
        departments (dict): Dictionary of departments and courses.
        command_args (list): List of strings containing department and optionally a course name.
                             Format: [department] or [department, course_name...]
    """
    if len(command_args) == 0:
        print("Invalid command!")
        return

    department = command_args[0]
    if department not in departments:
        print(f"Department {department} not found!")
        return

    if len(command_args) == 1:
        # Delete entire department
        del departments[department]
        print(f"Department {department} removed.")
    else:
        course_name = " ".join(command_args[1:])
        if course_name not in departments[department]:
            print(f"Course {course_name} from {department} not found!")
        else:
            del departments[department][course_name]
            print(f"Department {department} course {course_name} removed.")
            if not departments[department]:  # Remove department if empty
                del departments[department]


def main():
    """
    Main program function that manages course and department data.
    It reads the initial data from a file and supports the following commands:
    Add course, Credits of department, Delete course or department, Print all, Print department, and Quit.
    """
    filename = input("Enter file name: ").strip()
    departments = read_courses_from_file(filename)
    if departments is None:
        return

    while True:
        print()
        print("[A]dd / [C]redits / [D]elete / [P]rint all / p[R]int department / [Q]uit")
        command_line = input("Enter command: ").strip()
        if not command_line:
            print("Invalid command!")
            continue

        parts = command_line.split()
        command = parts[0].lower()
        args = parts[1:]

        if command == 'p':
            print()
            print_all(departments)
        elif command == 'r':
            if len(args) != 1:
                print("Invalid command!")
            else:
                print()
                print_department(departments, args[0])
        elif command == 'c':
            if len(args) != 1:
                print("Invalid command!")
            else:
                print()
                credits_of_department(departments, args[0])
        elif command == 'a':
            if len(args) < 3:
                print("Invalid command!")
            else:
                add_course(departments, args)
        elif command == 'd':
            if len(args) == 0:
                print("Invalid command!")
            else:
                delete_command(departments, args)
        elif command == 'q':
            print("Ending program.")
            break
        else:
            print("Invalid command!")


if __name__ == "__main__":
    main()