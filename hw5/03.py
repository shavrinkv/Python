import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(0,100,size=(10, 10)), columns=list('ABCDEFGHKL'))
df.index = ['Row_1', 'Row_2', 'Row_3', 'Row_4', 'Row_5', 'Row_6', 'Row_7', 'Row_8', 'Row_9', 'Row_10']
print(df
