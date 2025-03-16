print(12123)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# Загрузка датасета
data = pd.read_excel('data.xlsx')

# Предположим, что у вас есть столбцы 'полезная_работа' и 'затраченная_энергия'
data['Эффективность'] = (data['useful_calls_fact'] + data['useful_calls_fact'] +  data['avail_calls_fact'] + data['avail_chats_fact'] + data['avail_chat_call_fact'] + data['education_fact'])/(data['useful_calls_fact'] + data['useful_calls_fact'] +  data['avail_calls_fact'] + data['avail_chats_fact'] + data['avail_chat_call_fact'] + data['education_fact'] + data['break_fact'] + data['additional_fact'])

data['Продуктивность'] = (data['cnt_call'] + data['cnt_chat'])/(data['dlg_time_call'] + data['dlg_time_chat'])


print(data.head())

def plot_eff_by_parameter(parameter_column):
    """
    Plot average productivity grouped by values of the given parameter column.
    
    Args:
        parameter_column: The column name to group by
    """
    # Skip if the parameter is 'prod' itself or if it's not a categorical column
    if parameter_column == 'Эффективность':
        return
    
    # Group by the parameter and calculate mean productivity
    grouped_data = data.groupby(parameter_column)['Эффективность'].agg(['mean', 'count']).reset_index()
    
    # Sort by mean productivity for better visualization
    grouped_data = grouped_data.sort_values('mean')
    
    # Create figure
    plt.figure(figsize=(12, 6))
    
    # Create bar plot
    ax = sns.barplot(x=parameter_column, y='mean', data=grouped_data)
    
    # Add count annotations
    for i, row in enumerate(grouped_data.itertuples()):
        ax.text(i, row.mean + 0.01, f"n={row.count}", ha='center', va='bottom', fontsize=8)
    
    # Add labels and title
    plt.title(f'Average Eff by {parameter_column}', fontsize=14)
    plt.xlabel(parameter_column, fontsize=12)
    plt.ylabel('Average Eff', fontsize=12)
    
    # Rotate x-axis labels if needed
    plt.xticks(fontsize=9, rotation=45, ha='right')
    plt.yticks(fontsize=9)
    
    # Add grid for better readability
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()

# Loop through all columns and create plots
for column in data.columns:
    if column != 'Эффективность':  # Skip the productivity column itself
        try:
            print(f"Analyzing: {column}")
            plot_eff_by_parameter(column)
        except Exception as e:
            print(f"Error plotting {column}: {e}")
