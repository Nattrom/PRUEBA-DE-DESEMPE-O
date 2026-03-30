#🎓 Student Management System

###📌 Description

This is a console-based Python application designed to manage student information.
It allows users to perform basic CRUD operations (Create, Read, Update, Delete) and stores data persistently using a JSON file.

---

###🚀 Features

➕ Add new students
📋 View all students
🔍 Search students by ID or name
✏️ Update student information
🗑️ Delete students
💾 Data persistence using JSON
✅ Input validation (ID, name, age, status)

---

###🛠️ Technologies Used

Python 3
JSON for data storage

---

###📂 Project Structure

student_system/
│
├── main.py       # Main controller
├── menu.py       # User interface (menu)
├── crud.py       # CRUD operations
├── data.py       # Data persistence (JSON)
└── students.json # Data file (auto-generated)

---

###▶️ How to Run

Open the project folder in your terminal or VS Code
Make sure you have Python installed
Run the program:

python main.py

---

###💡 Example Usage

Select option "1" to add a student
Enter student details (ID, name, age, course, status)
Use option "2" to display all students
Use option "3" to search for a student
Use option "4" to update student information
Use option "5" to delete a student

---

###⚠️ Validations Implemented

ID must be numeric and unique
Name must contain only letters
Age must be between 1 and 120
Status must be "active" or "inactive"

---

###📦 Data Storage

Data is stored in a file called "students.json"
The file is automatically created and updated
Data persists between program executions

---

###👩‍💻 Author

Developed by Natalia Romerin Rincon 
    Clan: 8

---

###📄 License

This project is for educational purposes.
