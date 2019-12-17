import pandas as pd
import networkx as nx


path = 'uspatentcitation.tsv'

df = pd.read_csv(
    filepath_or_buffer = path,
    sep = '\t',
    nrows = 5000,
    usecols = ['patent_id', 'citation_id']
)

patent_dict = dict()

for index, row in df.iterrows():

    child = row['patent_id'].strip()
    parent = row['citation_id'].strip()

    citations = [
        child,
        parent
    ]

    patent_dict[child] = parent

graph = nx.DiGraph(patent_dict)
print(patent_dict)