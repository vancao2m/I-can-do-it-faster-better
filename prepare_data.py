# df stand for data frame name
-----------------------------------------------------------------------------------------------------------
# PREVIEW DATASET
# with the amount of data as large as nowadays,
# getting a pre-view of dataset is necessary as it avoid long waiting time and crashing system
# the packages used for both methods are pandas and numpy
import pandas as pd
import numpy as np

# 1: by slicing
import math
import collections
import matplotlib.pylot as pp

df[:10]

# 2: by heading
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
print(df.head(10))

# Comparison:
# the two method offer single line code however,
# I prefer "heading" as it doesnt require background knowledge on sclices in Python
-----------------------------------------------------------------------------------------------------------
# DEALING WITH DUPLICATES
# 1: using drop
df.drop_duplicates(inplace=True)

#2: changing from loop to set
df = set()
for line in open('df.txt','r'):
    df.add(line.strip().lower()
# OR:
df={line.strip().lower() for line in open('df.txt','r')}
# Comparison: I prefer using drop_duplicates as it shorter 
