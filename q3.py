set food=[]
set entertainment=[]
set transport=[]
function catagorise_expenses (expense):
for i in expense:
    if i<=40:
      entertainment=i
    elseif 40<i<=60:
      transport=i
    else:
      food=i
#user input
write ("enter your expenses", expense)
#function call
catagorise_expenses