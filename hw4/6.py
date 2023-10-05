import pandas as pd
df = pd.read_csv('all_ai_tool.csv')
print(df)


import re
result = re.findall(r' Mailbutler')
print(result)