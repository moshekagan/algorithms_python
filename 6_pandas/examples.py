import pandas as pd
import numpy as np


df = pd.DataFrame({ 'AAA' : [4,5,6,7], 'BBB' : [-10,-20,-30,-40], 'CCC' : [-100,-50,-30,-50] })
print(df)
print()
print(df.apply(np.cumsum))
print()
print(df.apply(np.cumsum, axis=1))