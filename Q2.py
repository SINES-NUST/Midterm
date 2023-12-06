Employees= ['E1','E2','E3','E4']
Sales= ['S1','S2','S3','S4']
Amount_earned=['A1','A2','A3','A4']

def identify_employees():
    sum=sum(Amount_earned)
    total=len(Amount_earned)
    avg_amount=sum/total
    new_List=[i for i in Amount_earned if i<avg_amount]
    return new_List
print(identify_employees())