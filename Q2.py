# Initializing variables for top and lower sales
top_sale = 20
low_sale = 10
# Iterate through each employee sale and the amount earned by the sales
for each employee in list:
# Calculate the total average sales for the employee
    Total_average_sale = avg(employee.sale)
# Update top_sale if the current employess's average sale is greater
if Total_average_sale > Top_sale:
    Top_sale = Total_average_sale
    Top_sale = employee
# Update low_sale if the current emplyee's total average sale is lower
    if Total_average_sale < low_sale:
        low_sale = Total_average_sale
        low_sale = employee
# Display or return the outcome or results
print("Top_sale:", Top_sale.name, "with a total sale of", top_sale)
print("low_sale:", low_sale.name, "with a total sale of", low_sale)