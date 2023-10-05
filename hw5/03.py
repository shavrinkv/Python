import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(0,100,size=(10, 10)), columns=list('ABCDEFGHKL')), index=('x', 'y')))
print(df)