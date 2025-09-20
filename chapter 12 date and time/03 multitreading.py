# multithreading = Used to perform multiple tasks concurrently

# IN this one threading.Thread(target = my_function) is very importe
import threading
import time


def wlak_dog(first):
    time.sleep(10)
    print(f"YOu finish walking {first}")

def take_out_trash():
    time.sleep(3)
    print("You take out the trash")

def get_mail():
    time.sleep(2)
    print("You get the mail")


chore1 = threading.Thread(target=wlak_dog,args=("pummpy",))

chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")