try:
    number = int(input("Enter number: "))

except ValueError:
    print("Invalid number")

else:
    print("Valid number: ", number)