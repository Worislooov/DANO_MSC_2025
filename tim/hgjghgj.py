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

# Рассчитываем количество людей в каждой скилл-группе
skill_group_size = df['skill_group'].value_counts().reset_index()
skill_group_size.columns = ['skill_group', 'group_size']

# Объединяем данные с количеством людей в скилл-группе
df = df.merge(skill_group_size, on='skill_group')

# Рассчитываем среднюю эффективность для каждой скилл-группы
mean_efficiency_by_skill_group = df.groupby('skill_group')['efficiency'].mean().reset_index()

# Объединяем данные с количеством людей и средней эффективностью
df_plot = mean_efficiency_by_skill_group.merge(skill_group_size, on='skill_group')

# Строим scatter plot
plt.figure(figsize=(10, 6))  # Размер графика
sns.scatterplot(
    x='group_size',      # Ось X: количество людей в скилл-группе
    y='efficiency',      # Ось Y: средняя эффективность
    data=df_plot,        # Данные
    alpha=0.7,           # Прозрачность точек
    color='blue'         # Цвет точек
)

# Добавляем линию тренда
sns.regplot(
    x='group_size',      # Ось X: количество людей в скилл-группе
    y='efficiency',      # Ось Y: средняя эффективность
    data=df_plot,        # Данные
    scatter=False,       # Не отображать точки
    color='red'          # Цвет линии тренда
)

# Добавляем заголовок и подписи осей
plt.title('Зависимость эффективности от количества людей в скилл-группе', fontsize=16)
plt.xlabel('Количество людей в скилл-группе', fontsize=12)
plt.ylabel('Средняя эффективность', fontsize=12)

# Добавляем сетку для удобства восприятия
plt.grid(True, linestyle='--', alpha=0.7)

# Показываем график
plt.show()
