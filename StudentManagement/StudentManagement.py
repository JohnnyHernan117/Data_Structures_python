class Student:
    def __init__(self, student_id, name, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades


class Node:
    def __init__(self, student):
        self.student = student
        self.next = None


class StudentLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, student):
        new_node = Node(student)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

    def delete_student(self, student_id):
        if self.head is None:
            print("The list is empty.")
            return

        # If the student to be deleted is the head
        if self.head.student.student_id == student_id:
            self.head = self.head.next
            print("Student with ID", student_id, "deleted.")
            return

        current = self.head
        while current.next:
            if current.next.student.student_id == student_id:
                current.next = current.next.next
                print("Student with ID", student_id, "deleted.")
                return
            current = current.next

        print("Student with ID", student_id, "not found.")

    def search_student(self, student_id):
        current = self.head
        while current:
            if current.student.student_id == student_id:
                print("Student found: ID:", current.student.student_id,
                      ", Name:", current.student.name,
                      ", Grades:", current.student.grades)
                return current.student
            current = current.next
        print("Student with ID", student_id, "not found.")
        return None

    def print_students(self):
        current = self.head
        if not current:
            print("No students in the system.")
            return
        while current:
            # Print student details directly
            print("ID:", current.student.student_id,
                  ", Name:", current.student.name,
                  ", Grades:", current.student.grades)
            current = current.next


# Example Usage
student_list = StudentLinkedList()

# Add students
student_list.insert_end(Student(1, "Alice", [85, 90, 95]))
student_list.insert_end(Student(2, "Bob", [75, 80, 70]))
student_list.insert_end(Student(3, "Charlie", [65, 85, 80]))

# Print all students
student_list.print_students()

# Search for a student by ID
student_list.search_student(2)

# Delete a student by ID
student_list.delete_student(2)

# Print all students after deletion
student_list.print_students()

