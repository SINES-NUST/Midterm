a = name of employee
b = sales
c = amount earned by sales
d = targets

#First we will define Dataframe function with four attributes
def Dataframe(a,b,c,d): #each attribute for each column in document
#We will assign the given document in a Dataframe by reading it.
Dataframe_Sales = df.read(document)
#Each column in the document is now a variable in the dataframe
#We can compare the sales with the target
    for i in (b):
        for j in (d):
            if df.sales < df.targets
                #we can add another variable to our dataframe called "Low Sales"
                #it will insert employee name who's sales do not meet the target
                LowSales = Dataframe_Sales.append()
#Then we can output the new column in Dataframe_Sales to view the employee with lowest sales that do not meet targets.
print(df.LowSales)

