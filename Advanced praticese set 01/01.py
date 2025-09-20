try:

    with open("9.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

    with open("0.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

    with open("6.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Thanks")