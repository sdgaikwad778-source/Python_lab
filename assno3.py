import pandas as pd
data = {
    'Name' : ['Vivek', 'Amit', 'Riya', 'Sneha', 'Rahul'],
    'Age' : [20,33,21,24,25],
    'Marks' : [85,90,78,92,88]
}
df = pd.DataFrame(data)
print("Original Dataframes: \n", df)