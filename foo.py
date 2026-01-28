import pandas as pd

df = pd.DataFrame({'a':[1,1,2,2,2], 'b':range(5,10), 'c':range(10,15)})
out = df.groupby('a').agg({'b':'mean', 'c':'median'})

out.to_csv('out.csv')
