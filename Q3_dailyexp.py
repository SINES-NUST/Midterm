#load file containing daily expenses
expenses= Load file containing daily Expenses
#initialize variables
food= [] hk
transport= []
entertainment= []
#sort the expenses into food, entertainment or transport
daily_cabFare= input ask the daily cab fare or subway fare?
Convert type of daily_cabFare to integer
movie_tic= input ask the price of movie ticket
Convert type of movie_tic to integer
for i in range expenses:
    if expenses == daily_cabFare:
       Append  expenses to transport
    elif expenses == movie_tic:
        Append  expenses to entertainment
    else:
        Append  expenses to food
    End if
End for
# print the lists that are output results
print Transportation expenses are: transport
print Entertainment expenses are: entertainment
print Food expenses are: food