import pandas as pd

# Загружаем данные
df = pd.read_excel('data.xlsx')

# Преобразуем стаж из месяцев в годы
df['exp_staff_years'] = df['exp_staff'] / 12

# Фильтруем сотрудников со стажем больше 17 лет
employees_over_17_years = df[df['exp_staff_years'] > 17]

# Выводим результат
print("Сотрудники со стажем больше 17 лет:")
print(employees_over_17_years[['id_employee', 'exp_staff', 'exp_staff_years']])

# Сохраняем результат в файл (опционально)
employees_over_17_years.to_excel('employees_over_17_years.xlsx', index=False)