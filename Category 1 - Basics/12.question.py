# Calculate income tax for the given income by following the below rules

"""
Taxable Income	                      Rate (in %)
First  $10,000	                      0
Next   $10,000	                      10
The remaining                       	20

"""

income = 45000
tax_payable = 0

print("Given Income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    tax_payable = (income - 10000) * 10 / 100
else:
    tax_payable = 0
    tax_payable = 10000 * 10 / 100

    tax_payable += (income - 20000) * 20 / 100

print("Total payable tax amount is", tax_payable)
