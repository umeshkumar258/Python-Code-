# ---------------------------------------
# STUDENT DETAILS PROGRAM
# ---------------------------------------

name = input("Enter the name: ")
marks = int(input("Enter the marks: "))
phone = input("Enter the phone number: ")

# Using format()
s = "The name of the student is {}, his marks are {}, and phone number is {}.".format(
    name, marks, phone
)

print(s)
