import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загружаем данные
df = pd.read_excel('data.xlsx')

# Группируем данные по skill_group и рассчитываем среднее значение skill_group_exp
mean_skill_group_exp_by_skill_group = df.groupby('skill_group')['skill_group_exp'].mean().reset_index()

# Сортируем данные по опыту для лучшей визуализации
mean_skill_group_exp_by_skill_group = mean_skill_group_exp_by_skill_group.sort_values(by='skill_group_exp', ascending=False)

# Выводим результат группировки
print(mean_skill_group_exp_by_skill_group)

# Строим barplot
plt.figure(figsize=(12, 6))  # Размер графика
sns.barplot(
    x='skill_group',          # Ось X: скилл-группа
    y='skill_group_exp',      # Ось Y: средний опыт в скилл-группе
    data=mean_skill_group_exp_by_skill_group,  # Данные
    palette='viridis'         # Цветовая палитра
)

# Добавляем заголовок и подписи осей
plt.title('Средний опыт в скилл-группе по группам', fontsize=16)
plt.xlabel('Скилл-группа', fontsize=12)
plt.ylabel('Средний опыт в скилл-группе (месяцы)', fontsize=12)

# Добавляем сетку для удобства восприятия
plt.grid(True, linestyle='--', alpha=0.7)

# Поворачиваем подписи на оси X для лучшей читаемости
plt.xticks(rotation=45, ha='right')

# Показываем график
plt.tight_layout()  # Улучшаем расположение элементов
plt.show()