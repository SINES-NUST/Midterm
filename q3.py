#Assigning variable
x = [food1, ent1, transport1, food2, ent2, transport2]
for i in x
    if  i has word food & transport
        continue
    print(i)
#ans [ent1, ent2]
for i in x
    if i has word ent & transport
        continue
    print (i)
#ans [food1, food2]
for i in x
    if i has word ent & food
        continue
    print (i)
#ans [transport1, transport2]