CG content = c
AT content = a
x = total CG content + AT sequences
x = c+a

#define CG content (x, a)
c = x-a
print(c)
return(c)

#Question 4 part 2
listx1 = [50]
listx2 = [801]
listx3 = [2000]
listx4 = [2938]
if x1, x2, x3, x4 are smaller than 2000
   print "non of the sequence is long"
elif x1, x2, x3, x4 are greater than 2938
    print "at least 1 variable is greater than 2938, so the greatest number is 2938"
else
#if the code reaches this block, the longest should be between 2000 and 2938
longest = max(x1, x2, x3, x4)
print "the greatest number among x1, x2, x3, x4 is, longest"
