DEFINE SALES(names, sales, amount_earned, target)
Initialize sum=0
calculate average of amount earned from sales
for elements in sale
    sum+=elements
average_of_sales=sum/len(sales)
for i from 0 to length of amount_earned
    if i is less than average_of_sales
        print names[i] has lower sales than average
    if i is greater than average_of_sales
        print names[i] has higher sales 
RETURN