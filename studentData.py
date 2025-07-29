class StudentFileReader:
    def __init__(self, student_num, last_name, first_name, gender, mark_obtained, level):
        self.student_num = student_num
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.mark_obtained = mark_obtained
        self.level = level

    def text_format(self):
        return f"{self.student_num} {self.last_name} {self.first_name} {self.gender} {self.mark_obtained} {self.level}\n"


#student data list
student_data = [
    (105, "Kabelo", "Joseph", "Male", 66, "Level 5"),
    (110, "Mampuru", "Dlamini", "Female", 90, "Level 7"),
    (120, "Smith", "John", "Male", 75, "Level 6")
]

#studentFileReader objects
students = [StudentFileReader(*data) for data in student_data]

#save students to a text file
with open("students.txt", "w") as file:
    for student in students:
        file.write(student.text_format())

print("Student data has been saved to students.txt successfully!")
