import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('data.xlsx')
correlation = df[['education_fact', 'useful_calls_fact', 'useful_chats_fact', 'dlg_time_call', 'dlg_time_chat']].corr()

# Визуализируем корреляционную матрицу
df['education_group'] = pd.cut(df['education_fact'], bins=[0, 1800, 3600, 5400, 7200, np.inf], labels=['<30 мин', '30-60 мин', '60-90 мин', '90-120 мин', '>120 мин'])

# Группируем и анализируем средние показатели
grouped = df.groupby('education_group')[['dlg_time_call', 'dlg_time_chat','cnt_call', 'cnt_chat']].mean()

print(grouped)

# Визуализируем результаты
grouped.plot(kind='bar', figsize=(12, 6))
plt.title('Средние показатели эффективности по группам обучения')
plt.xlabel('Группа обучения')
plt.ylabel('Среднее значение')
plt.show()