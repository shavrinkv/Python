import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(1,10,size=(10, 10)), columns=list('ABCDEFGHKL'))
print(df[df >= 5])