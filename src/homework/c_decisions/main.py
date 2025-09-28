from homework.c_decisions.decisions import get_letter_grade, get_letter_grade_switch

print("MAIN MENU")
print("1-Letter grade using if")
print("2-Letter grade using switch")
print("3-Exit")

choice = input("Enter your choice (1-3): ")

if choice in ['1', '2']:
    try:
        numerical_grade = int(input("Enter numerical grade (0-100): "))
        if numerical_grade >= 0 and numerical_grade <= 100:
            if choice == '1':
                print(f"Letter grade: {get_letter_grade(numerical_grade)}")
            else:
                print(f"Letter grade: {get_letter_grade_switch(numerical_grade)}")
        else:
            print("Number is out of range. Please enter a number between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
elif choice == '3':
    print("Exiting program.")
else:
    print("Invalid choice. Please select 1, 2, or 3.")