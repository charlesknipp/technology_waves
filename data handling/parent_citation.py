import pandas as pd
import numpy as np
from tqdm import tqdm


obs = 10000000

head = [
    'uuid','patent_id','citation_id','date','name','kind','country','category',
    'sequence'
]

for i in tqdm(range(1,11)):

    skipped = obs * i

    df_chunk = pd.read_csv(
        filepath_or_buffer = 'uspatentcitation.tsv',
        sep = '\t',
        header = None,
        names = head,
        usecols = ['patent_id','citation_id','date'],
        skiprows = skipped,
        nrows = obs,
        infer_datetime_format = True
    )

    df = df_chunk.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    path = 'chunks/data%d.csv' % i

    df.to_csv(
        path_or_buf = path,
        index = False
    )