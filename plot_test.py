# %% IMPORTS
import numpy as np
import matplotlib.pyplot as plt

# set global plot parameters:
plt.rcParams.update({'font.size':12})
plt.rcParams["axes.spines.top"]     = False
plt.rcParams["axes.spines.right"]     = False
plt.rcParams["axes.spines.bottom"]     = False
plt.rcParams["axes.spines.left"]     = False
# %% GENERATE SOME RANDOM DUMMY DATA
np.random.seed(1)
Group_A = np.random.randn(10)*10+5
Group_B = np.random.randn(10)*10+2
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
plt.ylim(-30, 30)
#plt.show()
fig.savefig("violinplot.pdf", dpi=120)
# %% FURTHER ANALYSIS
""" 
....
"""
# %% PLOTS (2)
# %% END