students = ["Shrikant", "Avi", "Parth", "Anteshwar", "Abc", "Xyz"]

# Accessing list elements
print(students)
print(students[0])
print(students[-1])

# Slicing
print(students[1:4])

# Changing list element
students[4] = "Pqr"
print(students)

# Adding element
students.append("John")
print(students)
students.insert(1, "Mark")
print(students)

# Removing list element
students.remove("Xyz")
print(students)
students.pop()
print(students)

# Sorting list
students.sort()
print(students)
students.reverse()
print(students)

# Iterating list
for student in students:
    print(student)