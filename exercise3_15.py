'''
1) Find the incident count of the top 10 precincts (‘ARREST_PRECINCT’ is the precinct ID where the incident occurred)
2) Store the top 10 precincts into a new dataframe with the precinct ID as an int column and the incident count as  another int column.
3) Plot the new dataframe, with the x-axis as precinct ID and the y-axis as incident/complaint count.
4) Find the top 10 incident descriptions 
('OFNS_DESC') by total count and print them. Store them in a separate dataframe with columns 'incident description' and 'incident count'. Plot the dataframe as you did above.
/Users/leahsanchez/Workspace/intro_to_python/NYPD_Arrests_Data__Historic_.csv
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/leahsanchez/Workspace/intro_to_python/NYPD_Arrests_Data__Historic_.csv', low_memory=False)
data.dataframeName = 'NYPD_Arrests_Data_Historic.csv'
data.shape
data.head()
data.describe()
print('info')
print(data.info())
# print(data)

# 1) Find the incident count of the top 10 precincts (‘ARREST_PRECINCT’ is the precinct ID where the incident occurred)
print(data['ARREST_PRECINCT'].value_counts())
part_1 = data['ARREST_PRECINCT'].value_counts().head(10)
print('Part 1: ')
print(part_1)

# 2) Store the top 10 precincts into a new dataframe with the precinct ID as an int column and the incident count as  another int column.

df2 = pd.DataFrame(part_1.reset_index().values, columns=["Precinct ID", "Incident Count"])
print('Part 2: ')
print(df2)

# 3) Plot the new dataframe, with the x-axis as precinct ID and the y-axis as incident/complaint count.
df2.plot(x="Precinct ID", y="Incident Count", kind='bar', rot=0)
# plt.show()

# 4) Find the top 10 incident descriptions ('OFNS_DESC') by total count and print them.  
# print(data['OFNS_DESC'].value_counts())
part_4 = data['OFNS_DESC'].value_counts().head(10)
print('Part 4.1: ')
print(part_4)

# Store them in a separate dataframe with columns 'incident description' and 'incident count'.
df3 = pd.DataFrame(part_4.reset_index().values, columns=["Incident Description", "Incident Count"])
print('Part 4.2: ')
print(df3)

# Plot the dataframe as you did above.
df3.plot(x="Incident Description", y="Incident Count", kind='bar',fontsize=6, rot=90)
plt.show()

