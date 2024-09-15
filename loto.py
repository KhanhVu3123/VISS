import random
import pandas as pd
import numpy as np
import os
import sys
from pathlib import Path

# Generate a dataframe of 50 loto sheets with 2 blank values on each row.
# Algorithm: Generate a 6*6 array, then choose 2 random places on the row then delete them.
random.seed(2003)

blank_lst = pd.DataFrame(columns=[None]*6)

script_path = Path(__file__).resolve()
script_dir = script_path.parent
os.chdir(script_dir)


# Generate the first 30 sheets of loto.
big_df = []
for k in range(30):
    lst1 = []
    for i in range(6):
        to_add = random.randint(1,9)
        while(to_add in lst1):
            to_add = random.randint(1,9)
        lst1.append(to_add)
    lst1.append(np.nan)
    lst2 = []
    for i in range(6):
        to_add = random.randint(10,19)
        while(to_add in lst2):
            to_add = random.randint(10,19)
        lst2.append(to_add)
    lst2.append(np.nan)

    lst3 = []
    for i in range(6):
        to_add = random.randint(20,29)
        while(to_add in lst3):
            to_add = random.randint(20,29)
        lst3.append(to_add)
    lst3.append(np.nan)

    lst4 = []
    for i in range(6):
        to_add = random.randint(30,39)
        while(to_add in lst4):
            to_add = random.randint(30,39)
        lst4.append(to_add)
    lst4.append(np.nan)

    lst5 = []
    for i in range(6):
        to_add = random.randint(40,49)
        while(to_add in lst5):
            to_add = random.randint(40,49)
        lst5.append(to_add)
    lst5.append(np.nan)

    lst6 = []
    for i in range(6):
        to_add = random.randint(50,60)
        while(to_add in lst6):
            to_add = random.randint(50,60)
        lst6.append(to_add)
    lst6.append(np.nan)


    df = np.array([lst1,lst2,lst3,lst4,lst5,lst6])

    df= df.T
    df = df.astype(np.float64)


    del11 = random.randint(0,5)
    del12 = random.randint(0,5)
    while(del12 == del11):
        del12 = random.randint(0,5)
    df[0,del11]= np.nan
    df[0,del12] = np.nan


    del21 = random.randint(0,5)
    del22 = random.randint(0,5)
    while(del22 == del21):
        del22 = random.randint(0,5)
    df[1,del21] = np.nan
    df[1,del22] = np.nan

    del31 = random.randint(0,5)
    del32 = random.randint(0,5)
    while(del32 == del31):
        del32 = random.randint(0,5)
    df[2,del31] = np.nan
    df[2,del32] = np.nan

    del41 = random.randint(0,5)
    del42 = random.randint(0,5)
    while(del42 == del41):
        del42 = random.randint(0,5)
    df[3,del41] =np.nan
    df[3,del42] = np.nan

    del51 = random.randint(0,5)
    del52 = random.randint(0,5)
    while(del52 == del51):
        del52 = random.randint(0,5)
    df[4,del51] = np.nan
    df[4,del52] = np.nan

    del61 = random.randint(0,5)
    del62 = random.randint(0,5)
    while(del62 == del61):
        del62 = random.randint(0,5)
    df[5,del61] = np.nan
    df[5,del62] = np.nan
    np.set_printoptions(threshold=sys.maxsize)

    df = pd.DataFrame(df)

    big_df.append(df)

# Generate a copied dataframe where each new sheet is basically a random combination of rows from sheet 1 to 30 generated above.
# We do this by generating a random order of 1 to 30 6 times which correspond to the order of the rows, which will then be the new 30 sheets.
# This way, at least 2 players are guaranteed to win. 
new_df_rows = [[] for _ in range(30)]

for row_idx in range(6):
    # Collect the rows at the current index from all original DataFrames
    rows_at_current_index = [df.iloc[row_idx] for df in big_df]
    # Shuffle the collected rows
    random.shuffle(rows_at_current_index)
    # Assign each shuffled row to the corresponding new DataFrame
    for i in range(30):
        new_df_rows[i].append(rows_at_current_index[i])

new_df_list = [pd.DataFrame(rows).reset_index(drop=True) for rows in new_df_rows]
for df in new_df_list:
    nan_row = pd.Series([np.nan] * df.shape[1], index=df.columns)
    df.loc[len(df)] = nan_row

print(new_df_list[0:3])
print(big_df[0:3])

#Combine the old and new DataFrames
combined_old_df = pd.concat(big_df, ignore_index=True)
combined_new_df = pd.concat(new_df_list, ignore_index=True)

# Combine both into one big DataFrame
big_df = pd.concat([combined_old_df, combined_new_df], ignore_index=True)

#Export the combined DataFrame to a CSV file
output_file_path = 'Loto.csv'  # Replace with your desired file path
big_df.to_csv(output_file_path, index=False)



    


    

