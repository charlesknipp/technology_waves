import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


path = 'chunks/data1.csv'

df = pd.read_csv(
    filepath_or_buffer = path,
    usecols = ['patent_id','citation_id']
)

# group by citation to show the most cited patents
df1 = df.groupby(['citation_id']).count()

# sort by the number of times the patent has been cited
print(df1.sort_values(by = ['patent_id']))