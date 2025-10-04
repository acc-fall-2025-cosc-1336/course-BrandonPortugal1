from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

def main():
    while True:
        print("\nHomework 4 Menu")
        print("1 - Factorial")
        print("2 - Sum odd numbers")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            while True:
                try:
                    num = int(input("Enter a number (1-9): "))
                    if 1 <= num <= 9:
                        break
                    else:
                        print("Number must be between 1 and 9.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            print(f"Factorial of {num} is {get_factorial(num)}")

        elif choice == "2":
            while True:
                try:
                    num = int(input("Enter a number (1-99): "))
                    if 1 <= num <= 99:
                        break
                    else:
                        print("Number must be between 1 and 99.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            print(f"Sum of odd numbers up to {num} is {sum_odd_numbers(num)}")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()