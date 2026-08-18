from concurrent.futures import ThreadPoolExecutor
import time


def walk_dog(dog_name: str) -> None:
    time.sleep(10)
    print(f"Finished walking {dog_name}.")


def take_out_trash() -> None:
    time.sleep(3)
    print("Took out the trash.")


def get_mail() -> None:
    time.sleep(2)
    print("Got the mail.")


def main():
    # Run tasks concurrently in a thread pool
    with ThreadPoolExecutor() as executor:
        executor.submit(walk_dog, "Pumpy")
        executor.submit(take_out_trash)
        executor.submit(get_mail)

    print("All chores are complete!")


if __name__ == "__main__":
    main()
