from __future__ import print_function
import pandas as pd
import pickle
import sys

# read the csv as a pandas dataframe by limiting the columns used

data_chunk = pd.read_csv(
    filepath_or_buffer = 'research/technology_waves/uspatentcitation.tsv',
    sep = '\t',
    iterator = True,
    usecols = ['uuid', 'patent_id', 'citation_id', 'date'],
    index_col = 'uuid',
    chunksize = 1000
)

# dictionary such that key == patent_id and row == citation_id

patent_dict = dict()
i = 0
print('Starting...')

# merge each chunk into the dictionary created above

for chunk in data_chunk:
    i += 1
    if i % 5 == 0:
        print(
            'Current Chunk: {} ({}% Complete)'.format(i, i/1000),
            end = '\r'
        )

    if i % 500 == 0:
        with open('patent_dict.pickle', 'wb') as handle:
            pickle.dump(
                patent_dict,
                handle,
                protocol = pickle.HIGHEST_PROTOCOL
            )

            f = open('current_chunk', 'w+')
            f.write('%d' % i)
            f.close()

    for _, data in chunk.iterrows():
        if data['patent_id'] not in patent_dict:
            patent_dict[data['patent_id']] = set()
        
        patent_dict[data['patent_id']].add(data['citation_id'])

# write it to a file to then filter the dictionary

with open('patent_dict.pickle', 'wb') as handle:
    pickle.dump(
        patent_dict,
        handle,
        protocol = pickle.HIGHEST_PROTOCOL
    )