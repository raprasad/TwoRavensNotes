
import pandas as pd

df = pd.read_csv('fearonLaitin.tsv', sep='\t', skipinitialspace=True).fillna(0)
open('fearonLaitin.csv', 'w').write(df.to_csv(index=False))
