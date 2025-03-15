import pandas as pd



# Создаем DataFrame
df = pd.read_excel('data.xlsx')

# Вычисляем среднее время работы по skill group
average_work_time = df.groupby('skill_group')['skill_group_exp'].mean().rename('average_work_time')

# Добавляем новый столбец в исходный DataFrame
df = df.join(average_work_time, on='skill_group')

print(df)