def check_person():
    words = {"umesh", "appu", "harry", "babu"}  # already lowercase

    name = input("Enter the name: ").strip().lower()

    if name in words:
        print("Good person")
    else:
        print("Bad person")


if __name__ == "__main__":
    check_person()
