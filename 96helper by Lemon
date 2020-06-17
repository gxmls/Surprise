import pandas as pd

import numpy as np

filename = "20200507-S2-1"

threshold = 0.05



df = pd.read_excel(filename + ".xlsx")

df.drop(df.tail(1).index,inplace=True)

start = df.index[df.iloc[:,0] == 'Wavel.'].tolist()[0]

end = df.last_valid_index()

df = df.iloc[start:end+1]

df.columns = df.iloc[0]

df.columns.name = None

df = df.set_index(df.columns[0])

df = df[1:]

df = df.astype(str).astype(int)

output = pd.DataFrame()

over_threshold = pd.DataFrame()

for i in range(0, len(df.columns), 2):

    col_alpha = df.iloc[:, i]

    col_beta = df.iloc[:, i+1]

    if col_beta.idxmax() != col_alpha.idxmax():

        print(col_alpha.name + " - " + col_beta.name + " has different max wave length!")

        change = round((col_beta.max() - col_alpha.max())/col_alpha.max(), 4)

        pair = col_alpha.name + " - " + col_beta.name + " Wavel. " + str(col_alpha.idxmax()) + " - "+str(col_beta.idxmax())

        data = pd.DataFrame({pair:[change]})

        data = data.set_index([pd.Series(['Change'])])

        output = pd.concat([output, data], axis = 1)

        if change > threshold or change < -threshold:

            data_over_threshold = data.set_index([pd.Series(['Change over '+ str(threshold)])])

            over_threshold =  pd.concat([over_threshold, data_over_threshold], axis = 1)

    else:

        change = round((col_beta.max() - col_alpha.max())/col_alpha.max(), 4)

        pair = col_alpha.name + " - " + col_beta.name + " Wavel. " + str(col_alpha.idxmax())

        data = pd.DataFrame({pair:[change]})

        data = data.set_index([pd.Series(['Change'])])

        output = pd.concat([output, data], axis = 1)

        if change > threshold or change < -threshold:

            data_over_threshold = data.set_index([pd.Series(['Change over '+ str(threshold)])])

            over_threshold =  pd.concat([over_threshold, data_over_threshold], axis = 1)

output.to_csv(filename + '_change.csv')

over_threshold.to_csv(filename + '_change.csv', mode='a', header=True)
