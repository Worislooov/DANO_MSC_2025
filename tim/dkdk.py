import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загружаем данные
df = pd.read_excel('data.xlsx')

# Рассчитываем эффективность
df['efficiency'] = (
    df['all_system_fact']-df['break_fact']-df['additional_fact']
) / df['all_system_fact']

# Удаляем строки с нулевыми значениями в знаменателе (если all_system_fact = 0)
df = df[df['all_system_fact'] > 0]

# Группируем данные по skill_group и рассчитываем среднее значение эффективности
mean_efficiency_by_skill_group = df.groupby('napravlenie')['efficiency'].mean().reset_index()

# Сортируем данные по эффективности для лучшей визуализации
mean_efficiency_by_skill_group = mean_efficiency_by_skill_group.sort_values(by='efficiency', ascending=False)

# Выводим результат группировки
print(mean_efficiency_by_skill_group)

# Строим barplot
plt.figure(figsize=(12, 6))  # Размер графика
sns.barplot(
    x='napravlenie',      # Ось X: скилл-группа
    y='efficiency',       # Ось Y: средняя эффективность
    data=mean_efficiency_by_skill_group,  # Данные
    palette='viridis'     # Цветовая палитра
)

# Добавляем заголовок и подписи осей
plt.title('Средняя эффективность по скилл-группам', fontsize=16)
plt.xlabel('Скилл-группа', fontsize=12)
plt.ylabel('Средняя эффективность', fontsize=12)

# Добавляем сетку для удобства восприятия
plt.grid(True, linestyle='--', alpha=0.7)

# Поворачиваем подписи на оси X для лучшей читаемости
plt.xticks(rotation=45, ha='right')

# Показываем график
plt.tight_layout()  # Улучшаем расположение элементов
plt.show()