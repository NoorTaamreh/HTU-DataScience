import pandas as pd

data = {
  "name": ["Sally", "Mary", "John"],
  "age": [50, 40, 30],
  "qualified": [True, False, False],
  "ID":[10,20,30]
}

df = pd.DataFrame(data)
print (df)

# newdf = df.drop("age", axis='columns')  #drop a column

# print(newdf)

# newdf2 = df.drop(0, axis='index')   #drop a row

# print(newdf2)


# df.drop(df.iloc[:, 1:3], inplace = True, axis = 1)
df3=df.drop(df.iloc[:, 1:2], inplace = False, axis = 1)
print (df3)


