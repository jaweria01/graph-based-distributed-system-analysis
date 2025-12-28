import pandas as pd
import os

print("Script started...")

# Get absolute path of current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build path to data file
data_path = os.path.join(BASE_DIR, "..", "data", "system_logs.csv")

print("Looking for file at:")
print(data_path)

# Load dataset
df = pd.read_csv(data_path)

print("\nDataset Loaded Successfully!")
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

# ✔ Relative vs absolute paths
# ✔ How Python locates files
# ✔ How to make code portable
# ✔ Best practice for research projects
