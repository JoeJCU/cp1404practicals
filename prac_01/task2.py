"""
Program to calculate and display a user's bonus based on sales.  
If sales are under $1,000, the user gets a 10% bonus.  
If sales are $1,000 or over, the bonus is 15%.  
"""

sales = float(input("Enter sales: $"))

if sales < 1000:
    bonus = sales * 0.10
    print(f"You will receive a bonus of ${bonus:.2f}")  # {bonus:.2f} formates the output 'bonus' to 2 decimal places
else:
    bonus = sales * 0.15
    print(f"You will receive a bonus of ${bonus:.2f}")
