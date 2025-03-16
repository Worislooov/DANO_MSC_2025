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

# Группируем данные по grafik и рассчитываем среднее значение эффективности
mean_efficiency_by_grafik = df.groupby('grafik')['efficiency'].mean().reset_index()

# Сортируем данные по эффективности для лучшей визуализации
mean_efficiency_by_grafik = mean_efficiency_by_grafik.sort_values(by='efficiency', ascending=False)

# Выводим результат группировки
print(mean_efficiency_by_grafik)

# Строим barplot
plt.figure(figsize=(12, 6))  # Размер графика
sns.barplot(
    x='grafik',          # Ось X: график работы
    y='efficiency',      # Ось Y: средняя эффективность
    data=mean_efficiency_by_grafik,  # Данные
    palette='viridis'    # Цветовая палитра
)

# Добавляем заголовок и подписи осей
plt.title('Средняя эффективность по графикам работы', fontsize=16)
plt.xlabel('График работы', fontsize=12)
plt.ylabel('Средняя эффективность', fontsize=12)

# Добавляем сетку для удобства восприятия
plt.grid(True, linestyle='--', alpha=0.7)

# Поворачиваем подписи на оси X для лучшей читаемости
plt.xticks(rotation=45, ha='right')

# Показываем график
plt.tight_layout()  # Улучшаем расположение элементов
plt.show()