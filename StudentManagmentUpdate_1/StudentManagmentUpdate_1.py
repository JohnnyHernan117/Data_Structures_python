import tkinter as tk
from tkinter import ttk, messagebox

# Array for storing course names (fixed size)
courses = ["Math", "Science", "English", "History", "Art"]

# Node class for Linked List
class StudentNode:
    def __init__(self, id, name, age, course):
        self.id = id
        self.name = name
        self.age = age
        self.course = course
        self.next = None

# Linked List class for storing student records dynamically
class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, id, name, age, course):
        new_student = StudentNode(id, name, age, course)
        if not self.head:
            self.head = new_student
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_student

    def delete_student(self, id):
        if not self.head:
            return False
        if self.head.id == id:
            self.head = self.head.next
            return True
        current = self.head
        while current.next and current.next.id != id:
            current = current.next
        if current.next:
            current.next = current.next.next
            return True
        return False

    def update_student(self, id, name, age, course):
        current = self.head
        while current:
            if current.id == id:
                current.name = name
                current.age = age
                current.course = course
                return True
            current = current.next
        return False

    def search_student(self, id):
        current = self.head
        while current:
            if current.id == id:
                return current
            current = current.next
        return None

    def get_all_students(self):
        students = []
        current = self.head
        while current:
            students.append(current)
            current = current.next
        return students

# Tkinter GUI
class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("700x500")

        # Linked List for storing student records
        self.student_list = StudentLinkedList()

        # Variables
        self.id_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.course_var = tk.StringVar()

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="Student Management System", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Input Section
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="ID:").grid(row=0, column=0, padx=10, pady=5)
        tk.Entry(input_frame, textvariable=self.id_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Name:").grid(row=1, column=0, padx=10, pady=5)
        tk.Entry(input_frame, textvariable=self.name_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Age:").grid(row=2, column=0, padx=10, pady=5)
        tk.Entry(input_frame, textvariable=self.age_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Course:").grid(row=3, column=0, padx=10, pady=5)
        course_combo = ttk.Combobox(input_frame, textvariable=self.course_var, state="readonly", values=courses)
        course_combo.grid(row=3, column=1, padx=10, pady=5)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add", command=self.add_student, width=12).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(button_frame, text="Update", command=self.update_student, width=12).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(button_frame, text="Delete", command=self.delete_student, width=12).grid(row=0, column=2, padx=10, pady=5)
        tk.Button(button_frame, text="Search", command=self.search_student, width=12).grid(row=0, column=3, padx=10, pady=5)
        tk.Button(button_frame, text="View All", command=self.view_all_students, width=12).grid(row=0, column=4, padx=10, pady=5)

        # Table Section
        self.table = ttk.Treeview(self.root, columns=("ID", "Name", "Age", "Course"), show="headings")
        self.table.heading("ID", text="ID")
        self.table.heading("Name", text="Name")
        self.table.heading("Age", text="Age")
        self.table.heading("Course", text="Course")
        self.table.pack(fill=tk.BOTH, expand=True, pady=10)

    def add_student(self):
        id = self.id_var.get()
        name = self.name_var.get()
        age = self.age_var.get()
        course = self.course_var.get()

        if not id or not name or not age or not course:
            messagebox.showerror("Error", "All fields are required!")
            return

        self.student_list.add_student(id, name, age, course)
        self.clear_fields()
        self.view_all_students()
        messagebox.showinfo("Success", "Student added successfully!")

    def delete_student(self):
        id = self.id_var.get()
        if not id:
            messagebox.showerror("Error", "Please enter the student ID to delete!")
            return

        if self.student_list.delete_student(id):
            self.view_all_students()
            self.clear_fields()
            messagebox.showinfo("Success", "Student deleted successfully!")
        else:
            messagebox.showerror("Error", "Student not found!")

    def update_student(self):
        id = self.id_var.get()
        name = self.name_var.get()
        age = self.age_var.get()
        course = self.course_var.get()

        if not id or not name or not age or not course:
            messagebox.showerror("Error", "All fields are required!")
            return

        if self.student_list.update_student(id, name, age, course):
            self.view_all_students()
            self.clear_fields()
            messagebox.showinfo("Success", "Student updated successfully!")
        else:
            messagebox.showerror("Error", "Student not found!")

    def search_student(self):
        id = self.id_var.get()
        if not id:
            messagebox.showerror("Error", "Please enter the student ID to search!")
            return

        student = self.student_list.search_student(id)
        if student:
            self.table.delete(*self.table.get_children())
            self.table.insert("", tk.END, values=(student.id, student.name, student.age, student.course))
        else:
            messagebox.showerror("Error", "Student not found!")

    def view_all_students(self):
        self.table.delete(*self.table.get_children())
        students = self.student_list.get_all_students()
        for student in students:
            self.table.insert("", tk.END, values=(student.id, student.name, student.age, student.course))

    def clear_fields(self):
        self.id_var.set("")
        self.name_var.set("")
        self.age_var.set("")
        self.course_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
