# Taking marks input
marks = int(input("Enter the marks: "))

# Checking grade
if marks >= 90 and marks <= 100:
    print("Excellent")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Grade D")
