import pandas as pd

data = {"A": [True, True, True],
        "B": [True, False, True]}
print("df:")
df = pd.DataFrame(data)
print(df)
print("------------------------")

print("df.all()")
print(df.all())
# A -> T
# B -> F
print("------------------------")

print("df.any()")
print(df.any())
# A -> T
# B -> T
print("------------------------")

print("df.all(axis=1)")
print(df.all(axis=1))
# 0 -> T
# 1 -> F
# 2 -> T
print("------------------------")

print("df.any(axis=1)")
print(df.any(axis=1))
# 0 -> T
# 1 -> F
# 2 -> T
print("------------------------")
