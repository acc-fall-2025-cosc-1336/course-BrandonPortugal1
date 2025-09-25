from output import get_sales_tax_amount, get_tip_amount

def main():
    
    try:
        meal_amount = float(input("Enter the meal amount: $"))
        tip_rate = float(input("Enter the tip rate percentage (e.g., 15 for 15%): "))
        
       
        sales_tax = get_sales_tax_amount(meal_amount)
        tip_amount = get_tip_amount(meal_amount, tip_rate)
        
        
        total = meal_amount + sales_tax + tip_amount
        
        
        print(f"\n{'-'*30}")
        print(f"Meal Amount:      {meal_amount:.2f}")
        print(f"Sales Tax:        {sales_tax:.2f}")
        print(f"Tip Amount:       {tip_amount:.2f}")
        print(f"Total:            {total:.2f}")
        print(f"{'-'*30}\n")
    
    except ValueError:
        print("Invalid input. Please enter numerical values.")


if __name__ == "__main__":
    main()