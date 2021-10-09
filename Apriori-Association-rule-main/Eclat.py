#Eclat

#Import Libraries
import pandas as pd

#Importing the dataset
dataset=pd.read_csv('Market_Basket_Optimisation.csv',header=None)
transactions=[]
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])

# Training the eclat on the dataset
from Eclat import eclat
rules=eclat.eclat(data=transactions,min_support=0.5)

#Visualizing the results
results=list(rules)