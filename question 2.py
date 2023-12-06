the document has 4 existing lists

-emp_names= <contains names of all employees>
-emp_sales= <contains details of sales made>
-amount_made= <contains details of amount earned>
-employ targets= <contains details of targets for employees>


# assume every index corresponds to same individual across all lists
# the amount lowest from the target amount will be best variable for such an identification


create a list off_targetamounts[]    #tells diff. in earned against target amount

off_targetamounts= employ_target - amount_made

avg_offtarget =mean(off_targetamounts)   # gives and avg value

low_sales=avg_offtarget[0]  # for comparision between elements

for item in  off_targetamounts
    if item < low_sales
        push off_targetamounts[item] in least_sale[]
        push emp_names[item] in least_salesemp[]

    else

    Do nothing

#    once the iteration of the loop is done
#    least_sales[] will only have values less than avg of overalloverall sales made
#    least_salesemp[] will only have corresponding names of the employees for whom least sales values are in least_sales
