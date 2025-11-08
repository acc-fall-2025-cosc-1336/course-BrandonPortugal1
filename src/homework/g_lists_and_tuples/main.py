from lists import get_lowest_list_value, get_highest_list_value

def get_user_numbers():
    numbers = []
    while True:
        try:
            num = float(input("Enter a list value: "))
            numbers.append(num)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if len(numbers) >= 3:
            cont = input("Do you want to enter another value? (y/n): ").strip().lower()
            if cont != 'y':
                break
    return numbers


def main():
    while True:
        print("\n--- MENU ---")
        print("1 - Show the list low/high values")
        print("2 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            nums = get_user_numbers()
            low = get_lowest_list_value(nums)
            high = get_highest_list_value(nums)
            print(f"\nLowest value: {low}")
            print(f"Highest value: {high}")
        elif choice == '2':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()