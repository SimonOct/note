def safeIntergerInput(prompt):
    inputString = input(prompt)
    try:
        number = int(inputString)
        return number
    except ValueError:
        print("Error in number format:", inputString)
        return safeIntergerInput(prompt)

if __name__ == "__main__":
    age = safeIntergerInput("Enter your age:")
    print("Your age is", age)