filename = "20200612 C292V-2"
import pandas as pd
import numpy as np

compare = pd.DataFrame(columns = ['Time'])
compare['Background'] = pd.read_csv(filename + " Background.csv", index_col = 0).loc[:, 'Mean'].reset_index(drop = True)
shotNum = compare['Background'].size
result = pd.read_csv(filename + " Results.csv", index_col = 0)
result['Areas']=result.loc[:, 'Area'].astype(str)
areas = result.loc[:, 'Areas'].drop_duplicates().tolist()

i = 1
for area in areas:
    mean = result.loc[result['Areas'] == area, 'Mean'].iloc[:shotNum].reset_index(drop = True)
    compare['Cell-'+str(i)+'_Mean'] = mean
    compare = compare.replace(np.nan, '', regex=True)
    i += 1
for i in range(1, len(areas)+1):
    compare['Cell-'+str(i)+'_Min'] = compare['Cell-'+str(i)+'_Mean'] - compare['Background']
    i += 1
compare.to_csv(filename+'.csv', index = False)

max_ = []
dr_ = [] 
column_index = []
for i in range(1, len(areas)+1):
    max_.append(compare['Cell-'+str(i)+'_Min'].max())
    dr_.append(((compare['Cell-'+str(i)+'_Min'].max()-compare['Cell-'+str(i)+'_Min'].iloc[0])/compare['Cell-'+str(i)+'_Min'].iloc[0])*100)
    column_index.append('Cell-'+str(i)+'_Min')
change = pd.DataFrame(list(zip(column_index, max_, dr_)), columns =['Cell','Max', 'DR']).set_index('Cell', drop=True)
change.to_csv(filename+'_change.csv')
print(filename+'.csv and '+filename+'_change.csv have been generated.')

