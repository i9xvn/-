class Student:
    def __init__(self, name, address, stage):
        self._name = name
        self._address = address
        self._stage = stage
    def __str__(self):
        return self._name
class Room:
    def __init__(self, number):
        self._number = number
        self._ss = []
    def add_student(self, student):
        if len(self._ss) < 4:
            self._ss.append(student)
            print(f"Added the student {student._name} to room {self._number}")
        else:
            print(f"Room {self._number} is full")
    def remove_student(self, name_student):
        for student in self._ss:
            if student._name == name_student:
                self._ss.remove(student)
                print(f"Removed {name_student} from room {self._number}.")
                return
        print(f"{name_student} not found in room {self._number}.")
    def display_students(self):
        if self._ss:
            print(f"Room {self._number} students:")
            for student in self._ss:
                print(f"Name: {student._name}, Address: {student._address}, Stage: {student._stage}")
        else:
            print(f"Room {self._number} has no students.")
class Wing:
    def __init__(self, name, supervisor):
        self._name = name
        self._supervisor = supervisor
        self._room = {i: Room(i) for i in range(1, 9)}
class Dormitory:
    def __init__(self):
        self._wings = {
            1: Wing('Wing 1', 'Hussein Salah'),
            2: Wing('Wing 2', 'Ali Majid'),
            3: Wing('Wing 3', 'Ali Kazem'),
            4: Wing('Wing 4', 'Abbas Nazem')}
    def add_student(self, wing_number, room_number, student_name, student_address, student_stage):
        if wing_number in self._wings and room_number in self._wings[wing_number]._room:
            student = Student(student_name, student_address, student_stage)
            self._wings[wing_number]._room[room_number].add_student(student)
        else:
            print("Invalid wing or room number.")
    def remove_student(self, wing_number, room_number, student_name):
        if wing_number in self._wings and room_number in self._wings[wing_number]._room:
            self._wings[wing_number]._room[room_number].remove_student(student_name)
        else:
            print("Invalid wing or room number.")
    def check_room(self, wing_number, room_number):
        if wing_number in self._wings and room_number in self._wings[wing_number]._room:
            room = self._wings[wing_number]._room[room_number]
            print(f"Room {room_number} in Wing {wing_number} (supervised by {self._wings[wing_number]._supervisor})")
            room.display_students()
        else:
            print("Invalid wing or room number.")
    def update_student_info(self, wing_number, room_number, student_name, new_address=None, new_stage=None):
        if wing_number in self._wings and room_number in self._wings[wing_number]._room:
            room = self._wings[wing_number]._room[room_number]
            for student in room._ss:
                if student._name == student_name:
                    if new_address:
                        student._address = new_address
                    if new_stage:
                        student._stage = new_stage
                    print(f"Updated {student_name}'s information.")
                    return
            print(f"Student {student_name} not found in room {room_number}.")
        else:
            print("Invalid wing or room number.")
def manage_dormitory():
    dorm = Dormitory()
    while True:
        print("\nOptions:")
        print("1: Add student")
        print("2: Remove student")
        print("3: Check room")
        print("4: Update student information")
        print("5: Exit")
        choice = input("Enter your choice (1-5): ")
        try:
            if choice == '1':
                wing_number = int(input("Enter wing number (1-4): "))
                room_number = int(input("Enter room number (1-8): "))
                student_name = input("Enter student name: ")
                student_address = input("Enter student address: ")
                student_stage = input("Enter student stage: ")
                dorm.add_student(wing_number, room_number, student_name, student_address, student_stage)
            elif choice == '2':
                wing_number = int(input("Enter wing number (1-4): "))
                room_number = int(input("Enter room number (1-8): "))
                student_name = input("Enter student name: ")
                dorm.remove_student(wing_number, room_number, student_name)
            elif choice == '3':
                wing_number = int(input("Enter wing number (1-4): "))
                room_number = int(input("Enter room number (1-8): "))
                dorm.check_room(wing_number, room_number)
            elif choice == '4':
                wing_number = int(input("Enter wing number (1-4): "))
                room_number = int(input("Enter room number (1-8): "))
                student_name = input("Enter student name: ")
                new_address = input("Enter new address (leave empty to skip): ")
                new_stage = input("Enter new stage (leave empty to skip): ")
                dorm.update_student_info(wing_number, room_number, student_name, new_address, new_stage)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
manage_dormitory()
