from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)

try:
    student = Student(name="Edward", surname="agle", id="toto")
except TypeError as e:
    print(f"{e.args[0]}")
