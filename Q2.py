# Generate the lists:
names_of_employee =['Ahmad', 'Ali', 'Irtaza', 'Ayesha', 'Anum']
sales = ['10,000', '20,000', '5,000', '15,000', '25,000']
amount_earned = ['4000', '10000', '2000', '8000', '19000']
target_sale = ['40,000']

# Calculate the average of the sales 
average = sum.sales / len(sales) 
print('Average sale is:', average)

# Identify employees whose sales are much lower
minimum_sale = [-1]
for i in sales:
    if minimum_sale < average:
        index = sales.index(minimum_sale)
        name_of_employee[index]
        print('Employee whose sale is much lower thanaverage:', name_of_employee)
    else:
        return(False)
    
    # Choose the best variable that will allow them
    # Generate correlation martrix
    import seaborns as sns 
    import matplotlib.pyplot as plt
    correlation = sns.corr('name of employee', 'sales', 'amount earned', 'target sale')
