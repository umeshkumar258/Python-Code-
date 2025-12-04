# try:
#     a = int(input("Hey,enter a number:"))
#     print(a)  


# except Exception as e:
#     print(e)

# finally:
#     print("hey i am inside finnlh")

def main():
    try:
        a = int(input("eneter the number: "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    

    finally:
        print("hey i a inside")


main()