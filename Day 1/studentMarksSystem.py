firstName = input("Enter First Name: ")
lastName = input("Enter Last Name: ")

maths = int(input("Enter Maths Marks: "))
english = int(input("Enter Engish Marks: "))
physics = int(input("Enter Physics Marks: "))

total = maths + english + physics

percentage = total / 3

if percentage > 75 :
    grade = "A"
elif percentage > 60 :
    grade = "B"
elif percentage > 40 :
    grade = "C"
else :
    grade = "Fail"


print("--------------------")
print("### Student Data ###")
print("Name: " + firstName + " " + lastName)
print(f"Maths: {maths} \nEnglish: {english} \nPhysics: {physics} \nTotal: {total}")
print("Percentage: ", percentage)
print("Grade: ", grade)