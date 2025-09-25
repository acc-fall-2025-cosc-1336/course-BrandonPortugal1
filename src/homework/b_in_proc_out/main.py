
from output import get_number, multiply_numbers

def main():
    num1 = get_number(7)
    num2 = get_number(7)
    print(f"{num1} x {num2} = {multiply_numbers(num1, num2)}")

    num3 = get_number(5)
    num4 = get_number(5)
    print(f"{num3} x {num4} = {multiply_numbers(num3, num4)}")

if __name__ == "__main__":
    main()

