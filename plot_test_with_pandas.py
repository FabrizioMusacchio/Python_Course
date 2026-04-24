# %% IMPORTS
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# set global plot parameters:
plt.rcParams.update({'font.size':12})
plt.rcParams["axes.spines.top"]     = False
plt.rcParams["axes.spines.right"]     = False
plt.rcParams["axes.spines.bottom"]     = False
plt.rcParams["axes.spines.left"]     = False
# %% READ DATA FROM FILES USING PANDAS
# np.random.seed(1)
# Group_A = np.random.randn(10)*10+5
# Group_B = np.random.randn(10)*10+2

file_path = "Data/Pandas_1/"

file_name_1 = "Group_A_data.xls"
file_name_2 = "Group_B_data.xls"

file_1 = os.path.join(file_path, file_name_1) # equivalent to:
                                              # file_1 = "Data/Pandas_1/Group_A_data.xls"
file_2 = os.path.join(file_path, file_name_2)

# Read the Excel files with Pandas into a Pandas Dataframe:
Group_A_df = pd.read_excel(file_1, index_col=0)
Group_B_df = pd.read_excel(file_2, index_col=0)

# extract the dataframe data to numpy arrays:
Group_A = Group_A_df["Data"].values
Group_B = Group_B_df["Data"].values

print(Group_A)
print(f"shape of Group_A: {Group_A.shape}")
# %% PLOTS
fig=plt.figure(3, figsize=(3.2, 3.5))
fig.clf()

plt.violinplot([Group_A, Group_B], showmedians=True)
plt.boxplot([Group_A, Group_B])

plt.xticks([1,2], labels=["A", "B"])

plt.xlabel("Groups")
plt.ylabel("measurements")
plt.title("Violin plot")

plt.tight_layout()
plt.ylim(-10, 70)
#plt.show()
fig.savefig("violinplot.pdf", dpi=120)
# %% FURTHER ANALYSIS
""" 
....
"""
# %% PLOTS (2)
# %% END