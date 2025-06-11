# Base class representing a general person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display basic details
    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Student class inheriting from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        # Call constructor of Person to initialize name and age
        super().__init__(name, age)
        self.student_id = student_id

    # Method to display student-specific details
    def show_student(self):
        print(f"Student ID: {self.student_id}")

# Teacher class also inheriting from Person (shows hierarchical inheritance)
class Teacher(Person):
    def __init__(self, name, age, subject):
        # Call constructor of Person
        super().__init__(name, age)
        self.subject = subject

    # Method to show teacher's subject
    def show_teacher(self):
        print(f"Teaches: {self.subject}")

# Independent class related to sports activities
class Sports:
    def __init__(self, sport_name):
        self.sport_name = sport_name

    # Method to show sport information
    def show_sport(self):
        print(f"Plays: {self.sport_name}")

# SportsStudent inherits from both Student and Sports (shows multiple inheritance)
class SportsStudent(Student, Sports):
    def __init__(self, name, age, student_id, sport_name):
        # Initialize Student part (which also initializes Person through super())
        Student.__init__(self, name, age, student_id)
        # Initialize Sports part
        Sports.__init__(self, sport_name)

    # Method to show all relevant details of a sports student
    def show_all(self):
        self.show_details()    # from Person
        self.show_student()    # from Student
        self.show_sport()      # from Sports

# Creating an object of SportsStudent (demonstrates hybrid inheritance)
player = SportsStudent("Abhay", 20, "S123", "Football")

# Displaying all information using the combined method
player.show_all()
