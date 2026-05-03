def check_name_length():
    name = input("Enter the name: ").strip()

    if len(name) > 10:
        print("Name has more than 10 characters")
    else:
        print("Name has 10 or fewer characters")


if __name__ == "__main__":
    check_name_length()
