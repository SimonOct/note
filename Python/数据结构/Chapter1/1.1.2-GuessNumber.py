import random
def main():
    smaller = int(input("Enter the smaller number:"))
    larger = int(input("Enter the larger number:"))
    myNumber = random.randint(smaller, larger)
    count = 0
    while True:
        count += 1
        userNumber = int(input("Enter your guess: "))
        if userNumber < myNumber:
            print("Too small")
        elif userNumber > myNumber:
            print("Too large")
        else:
            print("you've got it in", count, "tries!")
            break
if __name__ == "__main__":
    main()
    while True:
        retry = input("do you want to play agin?(y/n): ")
        if retry.lower() == "y" or retry.lower() == "yes":
            main()
        else:
            print("exited!")
            break
