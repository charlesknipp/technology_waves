import pandas as pd
import numpy as np
import json
from tqdm import tqdm
from collections import defaultdict

path = 'uspatentcitation.tsv'
patent_dict = dict()
rows = 0
i = 0
obs = 100000


pbar = tqdm(total = obs)

while rows <= obs: # 103835095
    i += 1
    rows = 1000 * i

    df_chunk = pd.read_csv(
        filepath_or_buffer = path,
        sep = '\t',
        usecols = ['patent_id', 'citation_id'],
        nrows = rows,
        infer_datetime_format = True
    )

    chunk_list = []

    for index, row in df_chunk.iterrows():

        child = row['patent_id'].strip()
        parent = row['citation_id'].strip()
        date = row['date'].strip()

        chunk = [
            child,
            parent,
            date
        ]

        chunk_list.append(chunk)

    for chunk in chunk_list:
        key = chunk[0]
        item = chunk[1]
        patent_dict[key] = item

    pbar.update(1000)

pbar.close()