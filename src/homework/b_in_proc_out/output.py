# Named constant for tax rate
TAX_RATE = 6.75 / 100  # 6.75%

# Function to calculate sales tax
def get_sales_tax_amount(meal_amount):
    return meal_amount * TAX_RATE

# Function to calculate tip amount
def get_tip_amount(meal_amount, tip_rate):
    return meal_amount * (tip_rate / 100)

