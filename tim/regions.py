import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data.xlsx')
# Рассчитываем количество сотрудников в каждом регионе
region_counts = df['residential_state_nm'].value_counts()

# Рассчитываем долю каждого региона
region_percentages = region_counts / region_counts.sum() * 100

# Объединяем регионы с долей меньше 2% в одну группу "остальные регионы"
small_regions = region_percentages[region_percentages < 2]
other_regions_count = small_regions.sum()
filtered_regions = region_percentages[region_percentages >= 2]
filtered_regions['Остальные регионы'] = other_regions_count

# Строим круговую диаграмму
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    filtered_regions,              # Данные для диаграммы
    labels=None,                   # Убираем подписи на секторах
    autopct='%1.1f%%',            # Формат отображения процентов
    startangle=90,                # Начальный угол (для красивого отображения)
    colors=plt.cm.YlOrBr(range(len(filtered_regions))),  # Используем палитру YlOrBr
    wedgeprops={'edgecolor': 'black', 'linewidth': 1},  # Границы между секторов
    textprops={'fontsize': 12},   # Увеличиваем размер шрифта
    shadow=True                   # Добавляем тень
)

# Добавляем подписи к секторам
for i, (wedge, label) in enumerate(zip(wedges, filtered_regions.index)):
    angle = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1  # Угол для размещения текста
    x = wedge.r * 0.8 * np.cos(np.deg2rad(angle))             # Координата X
    y = wedge.r * 0.8 * np.sin(np.deg2rad(angle))             # Координата Y
    ax.text(x, y, label, ha='center', va='center', fontsize=10, color='black')

# Добавляем легенду снаружи графика
plt.legend(
    filtered_regions.index,        # Названия регионов
    title="Регионы",              # Заголовок легенды
    loc="center left",            # Расположение легенды
    bbox_to_anchor=(1, 0.5)       # Смещение легенды за пределы графика
)

# Добавляем заголовок
plt.title('Доля сотрудников по регионам', fontsize=16)

# Увеличиваем расстояние между графиком и легендой
plt.tight_layout()

# Показываем график
plt.show()         