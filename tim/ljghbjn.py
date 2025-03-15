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

# Строим scatter plot с линией тренда
plt.figure(figsize=(10, 6))  # Размер графика
sns.scatterplot(
    x='additional_fact',  # Ось X: время на дополнительных активностях
    y='efficiency',       # Ось Y: эффективность
    data=df,              # Данные
    alpha=0.5,            # Прозрачность точек
    color='blue'          # Цвет точек
)

# Добавляем линию тренда
sns.regplot(
    x='additional_fact',  # Ось X: время на дополнительных активностях
    y='efficiency',       # Ось Y: эффективность
    data=df,              # Данные
    scatter=False,        # Не отображать точки
    color='red'           # Цвет линии тренда
)

# Добавляем заголовок и подписи осей
plt.title('Зависимость эффективности от времени на дополнительных активностях', fontsize=16)
plt.xlabel('Время на дополнительных активностях (секунды)', fontsize=12)
plt.ylabel('Эффективность', fontsize=12)

# Добавляем сетку для удобства восприятия
plt.grid(True, linestyle='--', alpha=0.7)

# Показываем график
plt.show()