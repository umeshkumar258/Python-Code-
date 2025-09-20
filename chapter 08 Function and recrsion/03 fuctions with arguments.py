def goodDay(name,ending):
    print("good Day " + name)
    print(ending)

goodDay("umesh","thanks")
goodDay("harry","thank you")



def goodDay(name,ending,new):
    print("good Day " + name + new)
    print(ending)
    return "done"
    

a = goodDay("umesh","thanks","hot")
print(a)

# Function to add two numbers
def new(number, number2):
    return number + number2

# Loop to take input and display results
for i in range(3):
    try:
        number = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        result = new(number, number2)
        print("The result is:", result)
    except ValueError:
        print("Invalid input. Please enter valid integers.")