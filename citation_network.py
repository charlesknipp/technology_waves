import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
from tqdm import tqdm


df = pd.read_csv(
    filepath_or_buffer = 'chunks/data0.csv',
    usecols = ['patent_id','citation_id']
)

for i in tqdm(range(1,11)):
    path = 'chunks/data%d.csv' % i
    df_c = pd.read_csv(
        filepath_or_buffer = path,
        usecols = ['patent_id','citation_id']
    )

    df = pd.concat([df_c, df])

# group by citation to show the most cited patents
df1 = df.groupby(['citation_id']).count()

# sort by the number of times the patent has been cited
print(df1.sort_values(by = ['patent_id']))