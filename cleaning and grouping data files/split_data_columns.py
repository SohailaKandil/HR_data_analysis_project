import pandas as pd

# Read the Excel file without specifying the header, as the header is embedded in the first row
data = pd.read_excel("Human_Resources_Cleaned_Data.xlsx", header=None)

# Split the first column into individual columns by comma
data_split = data.iloc[:, 0].str.split(',', expand=True)

# Set the first row as the column headers
data_split.columns = data_split.iloc[0]
data_split = data_split.drop(0)  # Drop the header row from the data

# Now you should have correctly split data
print(data_split.head())

data_split.to_excel("Human_Resources_Split_Data.xlsx", index=False)