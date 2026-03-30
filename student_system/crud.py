from data import * #import all data file

def add_student(students):
    """
    ADD A NEW STUDENT WITH VALIDATIONS.
    """
    #Validate ID(only numbers)
    while True:
        student_id=input("🪪​ Enter ID numbers only: ")
        if not student_id.isdigit():
            print("❌​ invalid ID. only numbers are allowed.")
            continue

        if any (s["id"]== student_id for s in students):
             print("❌ ID already exists.")
             continue
        break

    while True:
        name=input("👤 Enter name: ")
        if name.replace("","").isalpha():
            break
        else:
            print("❌​ Name must contain only letters.")

    #validate age
    while True:
        try:
            age=int(input("​🎂​ Enter age: "))
            break
        except ValueError:
            print("❌​ Age must be a number.")

    course=input("​📚​ Enter course: ")

    #Validate estatus
    while True:
        status=input("🕓​ Enter status (active or inactive): ").lower()
        if status in ["active", "inactive"]:
            break
        else:
            print("❌ Invalid status. Only active or inactive allowed.")

    #create student dicionary
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "status": status
        }
    
    #add to list
    students.append(student)
    from data import save_students
    #Save data
    save_students(students)
    
    print("✅ Student added successfully")

def list_students(students):
    """
    Display all students.
    """
    if not students:
        print("📭​ No students found.\n")
        return

    print("\n📋​ STUDENT LIST: ")
    for s in students:
        print(f"🆔​ {s['id']} | 👤 {s['name']} | 🎂 {s['age']} | 📚 {s['course']} | 🕓 {s['status']}")
    print()


def find_student(students):
    """
    Find a student by ID or name
    """
    search = input("👤 Enter ID or name: ").lower()

    results = [
        s for s in students
        if s["id"] == search or s["name"].lower() == search
    ]

    if results:
        print("\n✅​ Student found: ")
        for s in results:
            print(f"🆔​ {s['id']} | 👤 {s['name']} | 🎂 {s['age']} | 📚 {s['course']} | 🕓 {s['status']}")
        else:
            print("❌​ Student no found.")
        print()

def update_student(students):
    """
    Update and existing student.
    """
    student_id = input("🆔 Enter ID to update: ")

    for s in students:
        if s["id"] == student_id:

            print("⚠️​ Leave black to keep")
            
            #update fields (or keep current values)
            name = input(f"👤 New name ({s['name']}): ") or s["name"]
            age_input = input(f"🎂 New age ({s['age']}): ")
            course = input(f"📚 New course ({s['course']}): ") or s["course"]
            status = input(f"🕓​ New status ({s['status']}): ") or s["status"]

            #valide age if changed
            try:
                age = int(age_input) if age_input else s["age"]
            except ValueError:
                print("❌ invalid age. Keeping previus value.")
                age = s["age"]

            #update diccionary
            s.update({
                "name": name,
                "age": age,
                "course": course,
                "status": status
            })

            save_students(students)
            print("✅​ Student updated.\n")
            return

    print("❌ Student not found.\n")

def delete_student(students):
    student_id = input("🗑️​ Enter ID to delete: ")

    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            save_students(students)
            print("✅ ​Student deleted.\n")
            return

    print("❌ Student not found.\n")