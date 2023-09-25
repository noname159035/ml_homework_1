import numpy as np
import pandas as pd
import matplotlib

df = pd.read_csv('titanic.csv', sep=',', header=None)
# df = df.drop(labels = [0],axis = 0)

print(df)

print(f"Ответ на 1 вопрос: {len(df.values) - 1}")
df_sex = df[4]
print(f"Ответ на 1 вопрос:")
print(f"Мужчин - {len(df_sex[df_sex == 'male'])}")
print(f"Женщин - {len(df_sex[df_sex == 'female'])}")

df_surv = df[1]
print(f"Ответ на 2 вопрос:")
print(f"процент выживших - {len(df_surv[df_surv == '1']) / len(df_surv)}")

# df_1_class = df[2]
# print(f"Ответ на 2 вопрос:")
# df.groupby(['Pclass']).sum().plot(kind='pie', y='Pclass')
