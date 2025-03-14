import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


# 1. Функция для быстрого просмотра статистики данных
def quick_stats(df):
    print("═"*50)
    print("Basic Information:")
    print(df.info())
    
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    print("\nDescriptive Statistics:")
    print(df.describe(include='all'))
    
    print("\nUnique Values:")
    print(df.nunique())

# 2. Функция для построения распределения числовых переменных
def plot_distributions(df, numerical_cols, n_cols=3, figsize=(20, 15)):
    n_rows = int(np.ceil(len(numerical_cols)/n_cols))
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
    axes = axes.flatten()
    
    for i, col in enumerate(numerical_cols):
        sns.histplot(df[col], kde=True, ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
    plt.tight_layout()
    plt.show()

# 3. Матрица корреляций с heatmap
def plot_correlation_matrix(df, numerical_cols, figsize=(12, 10)):
    corr = df[numerical_cols].corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    plt.figure(figsize=figsize)
    sns.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='coolwarm',
                vmin=-1, vmax=1, linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()

# 4. Анализ категориальных переменных
def analyze_categorical(df, categorical_cols, top_n=5):
    for col in categorical_cols:
        print(f"\n═"*50)
        print(f"Analysis for {col}:")
        print(df[col].value_counts(dropna=False).head(top_n))
        
        plt.figure(figsize=(10, 5))
        df[col].value_counts(normalize=True).head(top_n).plot(kind='bar')
        plt.title(f'Top {top_n} Categories in {col}')
        plt.show()

# 5. Boxplot для анализа распределений по категориям
def plot_category_boxplots(df, numerical_col, categorical_col, figsize=(12, 8)):
    plt.figure(figsize=figsize)
    sns.boxplot(x=categorical_col, y=numerical_col, data=df)
    plt.xticks(rotation=45)
    plt.title(f'{numerical_col} distribution by {categorical_col}')
    plt.show()

# 6. Поиск выбросов с помощью IQR
def detect_outliers_iqr(df, numerical_cols, threshold=1.5):
    outlier_info = {}
    for col in numerical_cols:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - threshold*iqr
        upper_bound = q3 + threshold*iqr
        
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        outlier_info[col] = {
            'count': len(outliers),
            'percentage': len(outliers)/len(df)*100,
            'lower_bound': lower_bound,
            'upper_bound': upper_bound
        }
    return pd.DataFrame(outlier_info).T

# 7. Парные диаграммы рассеяния
def plot_scatter_matrix(df, numerical_cols, figsize=(20, 20), alpha=0.5):
    sns.pairplot(df[numerical_cols], diag_kind='kde', plot_kws={'alpha': alpha})
    plt.suptitle('Scatter Plot Matrix', y=1.02)
    plt.show()

# 8. Анализ временных рядов (если есть datetime колонка)
def analyze_time_series(df, date_col, value_col, freq='D', figsize=(16, 8)):
    df = df.set_index(date_col).sort_index()
    resampled = df[value_col].resample(freq).mean()
    
    plt.figure(figsize=figsize)
    resampled.plot(title=f'{value_col} over Time ({freq} frequency)')
    plt.ylabel(value_col)
    plt.show()

# 9. Сравнение групп с t-тестом
def perform_t_test(df, group_col, value_col, group_a, group_b):
    group1 = df[df[group_col] == group_a][value_col]
    group2 = df[df[group_col] == group_b][value_col]
    
    t_stat, p_value = stats.ttest_ind(group1, group2, nan_policy='omit')
    
    print(f"T-test between {group_a} and {group_b}:")
    print(f"T-statistic: {t_stat:.4f}")
    print(f"P-value: {p_value:.4f}")
    print("─"*50)
    return t_stat, p_value

# 10. Круговые диаграммы для категориальных переменных
def plot_pie_chart(df, categorical_col, figsize=(8, 8), limit=0.02):
    counts = df[categorical_col].value_counts()
    other = counts[counts/len(df) < limit].sum()
    counts = counts[counts/len(df) >= limit]
    counts['Other'] = other
    
    plt.figure(figsize=figsize)
    counts.plot(kind='pie', autopct='%1.1f%%')
    plt.title(f'Distribution of {categorical_col}')
    plt.ylabel('')
    plt.show()

# 11. Автоматический отчет профилирования данных
def generate_profiling_report(df, title='Data Profiling Report', file_name='report.html'):
    pass

# 12. Анализ парных взаимодействий с тепловой картой
def plot_pairwise_heatmap(df, group_col, value_col, figsize=(12, 8)):
    pivot_table = df.pivot_table(values=value_col, 
                               index=group_col, 
                               columns=group_col,
                               aggfunc='mean')
    
    plt.figure(figsize=figsize)
    sns.heatmap(pivot_table, annot=True, fmt=".1f", cmap="viridis")
    plt.title(f'Pairwise {value_col} Comparison')
    plt.show()

# Пример использования:
if __name__ == "__main__":
    # Загрузка данных
    df = pd.read_excel('data/example.xlsx')
    
    # Вызов функций
    quick_stats(df)
    plot_distributions(df, df.select_dtypes(include=np.number).columns.tolist())
    plot_correlation_matrix(df, df.select_dtypes(include=np.number).columns.tolist())