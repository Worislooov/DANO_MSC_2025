import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загружаем данные
df = pd.read_excel('data.xlsx')

# Рассчитываем эффективность
df['efficiency'] = (
    df['useful_chats_fact'] + df['useful_calls_fact'] + 
    df['avail_chat_call_fact'] + df['avail_chats_fact'] + 
    df['avail_calls_fact'] + df['education_fact']
) / df['all_system_fact']

# Удаляем строки с нулевыми значениями в знаменателе (если all_system_fact = 0)
df = df[df['all_system_fact'] > 0]

# Рассчитываем средний опыт в скилл-группе для каждой скилл-группы
mean_skill_group_exp_by_skill_group = df.groupby('skill_group')['skill_group_exp'].mean().reset_index()

# Объединяем данные с средним опытом в скилл-группе
df = df.merge(mean_skill_group_exp_by_skill_group, on='skill_group', suffixes=('', '_mean'))

# Строим lineplot
plt.figure(figsize=(10, 6))  # Размер графика
sns.lineplot(
    x='skill_group_exp_mean',  # Ось X: средний опыт в скилл-группе
    y='efficiency',            # Ось Y: эффективность
    data=df,                   # Данные
    ci='sd',                   # Доверительный интервал (стандартное отклонение)
    color='blue',              # Цвет линии
    estimator='mean'           # Используем среднее значение для агрегации
)

# Добавляем заголовок и подписи осей
plt.title('Зависимость эффективности от среднего опыта в скилл-группе', fontsize=16)
plt.xlabel('Средний опыт в скилл-группе (месяцы)', fontsize=12)
plt.ylabel('Эффективность', fontsize=12)

# Добавляем сетку для удобства восприятия
plt.grid(True, linestyle='--', alpha=0.7)

# Показываем график
plt.show()