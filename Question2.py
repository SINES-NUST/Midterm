#Question 2
#A sales company wants to identify employees whose sales are much lower than the average sales.
#They have a document that lists the name of the employee, the sales and the amount earned by the sales,
#they also have the targets given, choose the best variable that will allow them to identify the 
#requirement above

name = ["Jane", "Zara", "Sarah", "Joe", "Nick", "Jack"]
sale = [5, 7, 10, 2, 12, 4]

sum_sale = 5 + 7 + 10 + 2 + 12 + 4
avg_sale = sum_sale/6
calc_sale = sale/avg_sale

if calc_sale < 0.5:
    index = calc_sale.index
    name_call = name([(index)])
    print(name_call)
else:
    print("sales are ok!")