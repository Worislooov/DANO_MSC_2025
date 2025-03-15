import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Загружаем данные
df = pd.read_excel('data.xlsx')



# Функция для удаления выбросов с использованием IQR
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)  # Первый квартиль (25%)
    Q3 = df[column].quantile(0.75)  # Третий квартиль (75%)
    IQR = Q3 - Q1                   # Межквартильный размах

    # Определяем границы для выбросов
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Фильтруем данные, оставляя только значения в пределах границ
    filtered_df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return filtered_df

# Пример: Очистка столбцов от выбросов
columns_to_clean = ['useful_calls_fact', 'useful_chats_fact', 'education_fact', 'exp_staff']

# Применяем функцию к каждому столбцу
for column in columns_to_clean:
    df = remove_outliers_iqr(df, column)


# Сохраняем очищенные данные в новый файл (опционально)
df.to_excel('cleaned_data.xlsx', index=False)
# Рассчитываем фактическое полезное время
df['useful_time_fact'] = df['useful_calls_fact'] + df['useful_chats_fact']

# Рассчитываем плановое полезное время
df['useful_time_plan'] = df['work_activity_plan']

# Определяем переработку
df['overtime'] = df['useful_time_fact'] - df['useful_time_plan']

# Создаем признак переработки (1 — есть переработка, 0 — нет)
df['has_overtime'] = df['overtime'].apply(lambda x: 1 if x > 0 else 0)

# Группируем по стажу и рассчитываем процент переработок
overtime_by_exp = df.groupby('exp_staff')['has_overtime'].mean() * 100

# Преобразуем результат в DataFrame для удобства
overtime_by_exp = overtime_by_exp.reset_index()
overtime_by_exp.columns = ['exp_staff', 'overtime_percent']

# Строим график
plt.figure(figsize=(10, 6))  # Размер графика
sns.lineplot(
    x='exp_staff',          # Стаж сотрудника
    y='overtime_percent',   # Процент переработок
    data=overtime_by_exp,   # Данные
    marker='o',             # Маркеры для точек
    color='blue'            # Цвет линии
)

# Добавляем заголовок и подписи осей
plt.title('Зависимость процента переработок от стажа в компании', fontsize=16)
plt.xlabel('Стаж сотрудника (месяцы)', fontsize=12)
plt.ylabel('Процент переработок (%)', fontsize=12)

# Добавляем сетку для удобства восприятия
plt.grid(True, linestyle='--', alpha=0.7)

# Показываем график
plt.show()