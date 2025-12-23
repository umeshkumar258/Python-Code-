# Multithreading = Used to perform multiple tasks concurrently
# threading.Thread(target=function_name, args=()) is very important

import threading
import time


def walk_dog(dog_name):
    time.sleep(10)
    print(f"You finished walking {dog_name}")


def take_out_trash():
    time.sleep(3)
    print("You took out the trash")


def get_mail():
    time.sleep(2)
    print("You got the mail")


# Create threads
chore1 = threading.Thread(target=walk_dog, args=("Pumpy",))
chore2 = threading.Thread(target=take_out_trash)
chore3 = threading.Thread(target=get_mail)

# Start threads
chore1.start()
chore2.start()
chore3.start()

# Wait for all threads to complete
chore1.join()
chore2.join()
chore3.join()

print("✅ All chores are complete!")
