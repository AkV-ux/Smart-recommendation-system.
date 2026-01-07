import pandas as pd

# Load data
data = pd.read_csv("data/movies.csv")


print("Dataset Preview:")
print(data.head())

print("\nDataset Info:")
print(data.info())

print("\nAverage Rating per Genre:")
print(data.groupby("genre")["rating"].mean())
