import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors


class GradeTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grade Tracker")

        # Grades list to store subject-grade tuples
        self.grades = []

        # UI Components
        self.setup_ui()

    def setup_ui(self):
        # Student Details
        tk.Label(self.root, text="Student Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Roll Number:").grid(row=1, column=0, padx=10, pady=5)
        self.roll_entry = tk.Entry(self.root)
        self.roll_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Class:").grid(row=2, column=0, padx=10, pady=5)
        self.class_entry = tk.Entry(self.root)
        self.class_entry.grid(row=2, column=1, padx=10, pady=5)

        # Subject and Marks Input
        tk.Label(self.root, text="Subject:").grid(row=3, column=0, padx=10, pady=10)
        self.subject_entry = tk.Entry(self.root)
        self.subject_entry.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(self.root, text="Marks:").grid(row=4, column=0, padx=10, pady=10)
        self.marks_entry = tk.Entry(self.root)
        self.marks_entry.grid(row=4, column=1, padx=10, pady=10)

        # Buttons
        tk.Button(self.root, text="Add Marks", command=self.add_marks).grid(row=5, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Calculate Grades", command=self.calculate_grades).grid(row=5, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Generate Grade Card", command=self.generate_grade_card).grid(row=5, column=2, padx=10, pady=10)
        tk.Button(self.root, text="Clear Selected", command=self.clear_selected).grid(row=6, column=0, padx=10, pady=10)
        tk.Button(self.root, text="Clear All", command=self.clear_all).grid(row=6, column=1, padx=10, pady=10)

        # Listbox to display grades
        self.grades_list = tk.Listbox(self.root, width=50)
        self.grades_list.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

    def determine_grade(self, marks):
        """Determine grade based on marks."""
        if marks < 33:
            return "F"
        elif marks < 40:
            return "D"
        elif marks < 50:
            return "C"
        elif marks < 60:
            return "B"
        elif marks < 70:
            return "A-"
        elif marks < 80:
            return "A"
        else:
            return "A+"

    def add_marks(self):
        subject = self.subject_entry.get()
        marks = self.marks_entry.get()

        if not subject or not marks:
            messagebox.showerror("Input Error", "Please enter both subject and marks.")
            return

        try:
            marks = float(marks)
            if marks < 0 or marks > 100:
                raise ValueError
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid marks between 0 and 100.")
            return

        grade = self.determine_grade(marks)
        self.grades.append((subject, marks, grade))
        self.grades_list.insert(tk.END, f"{subject}: {marks} - {grade}")

        self.subject_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)

    def calculate_grades(self):
        if not self.grades:
            messagebox.showinfo("No Grades", "No grades available to calculate.")
            return

        # Calculate total marks and average marks
        total_marks = sum(marks for _, marks, _ in self.grades)
        average_marks = total_marks / len(self.grades)

        # Check for failure
        failed_subjects = [grade for _, _, grade in self.grades if grade == "F"]
        average_grade = "F" if failed_subjects else self.determine_grade(average_marks)

        # Display results
        result_message = (
            f"Average Marks: {average_marks:.2f}\n"
            f"Average Grade: {average_grade}"
        )
        if failed_subjects:
            result_message += "\nResult: Failed"
        else:
            result_message += "\nResult: Passed"

        messagebox.showinfo("Result", result_message)

    def clear_selected(self):
        selected_index = self.grades_list.curselection()
        if selected_index:
            self.grades_list.delete(selected_index)
            del self.grades[selected_index[0]]

    def clear_all(self):
        self.grades.clear()
        self.grades_list.delete(0, tk.END)

    def generate_grade_card(self):
        if not self.grades:
            messagebox.showerror("No Data", "No grades to generate a grade card.")
            return

        student_name = self.name_entry.get().strip()
        roll_number = self.roll_entry.get().strip()
        student_class = self.class_entry.get().strip()

        if not student_name or not roll_number or not student_class:
            messagebox.showerror("Input Error", "Please fill in all student details.")
            return

        # Calculate averages
        total_marks = sum(marks for _, marks, _ in self.grades)
        average_marks = total_marks / len(self.grades)
        failed_subjects = [grade for _, _, grade in self.grades if grade == "F"]
        average_grade = "F" if failed_subjects else self.determine_grade(average_marks)

        # PDF file name
        pdf_name = f"{student_name}_grade_card.pdf"

        # Create PDF
        pdf = SimpleDocTemplate(pdf_name, pagesize=letter)
        elements = []

        # Add header with student details
        header_data = [
            ["Student Name:", student_name],
            ["Roll Number:", roll_number],
            ["Class:", student_class],
        ]
        for item in header_data:
            elements.append(Table([item], style=TableStyle([("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold")])))

        elements.append(Table([[""]]))  # Empty row for spacing

        # Add grades table
        table_data = [["Subject", "Marks", "Grade"]]
        table_data.extend(self.grades)
        table_data.append(["", "Average Marks", f"{average_marks:.2f}"])
        table_data.append(["", "Average Grade", average_grade])

        table = Table(table_data)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(table)

        # Build and save the PDF
        try:
            pdf.build(elements)
            messagebox.showinfo("Success", f"Grade card generated: {pdf_name}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate PDF: {e}")



# Initialize the Tkinter root and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = GradeTrackerApp(root)
    root.mainloop()
