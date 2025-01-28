import pandas as pd
import glob
import os

# Directory containing the CSV files
directory = r"C:\Users\nikoa\Documents\ML ClimateChange\Climate-Change-Analysis\data"

# Read all CSV files in the directory
all_files = glob.glob(os.path.join(directory, "*.csv"))

df_1=pd.read_csv(all_files[0])
print(df_1.info())
#Muestra la columna numero 1
print(df_1.iloc[:,3])