List=[1,2,'a',22.4,'b',3,91.9,'c',14.12]
for i in List:
    if i==int:
        print(f'{i} is food expense')
        continue
    elif i=='str':
        print(f'{i} is travel expense')
        continue
    elif i=='float':
        print(f'{i} is entertainment expense')
        continue
    else:
        print()
#to categorize in a new_list_
new_List=[[i,j,k] for i in List if i==int for j in List if j=='str' for k in List if k==float]
print(new_List)