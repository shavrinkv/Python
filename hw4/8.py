import pandas as pd
import numpy as np

df = pd.read_csv('./nlo.csv')
country_count = pd.value_counts(df['country'].values, sort=True)
country_count_keys, country_count_values = dict_sort(dict(country_count))