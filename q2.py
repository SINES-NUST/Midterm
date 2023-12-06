initialize variable 'name_employee' as list to store employee names that are given.
initialize variable 'sale_amount' as list to store amount sold by each employee given in document.
initialze variable 'target' and set random target value as per document.
initialize variable 'low_sale_employee' to store names of employees with sale amount less than target while in a loop.

#it will look like 
name_employee=['eman','nasir','ayesha', 'adil']
sale_amount=['10000','9000','8000','20000']
target=['10000']
low_sale_employee=[]

iterate through 'sale_amount' list length:
    if i in sale_amount<target
        append 'low_sale_employee' list by adding 'name_employee' list at same index
    else
        continue
end Loop 
print 'low_sale_employee' list  