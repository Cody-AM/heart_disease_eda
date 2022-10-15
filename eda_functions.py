import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from collections import Counter

def categorical_percentage_bars(var_df, x_var, percentages):
    total_bars = np.full((len(var_df)), 100)
    f, ax = plt.subplots(figsize=(15, 8))
    sns.barplot(x=x_var, y=total_bars, label='Total', color='#66c2a5')
    sns.barplot(x=x_var, y=percentages, label='Have Had Heart Disease', color='#fc8d62')
    ax.set_title('Percentages That Have Had Heart Disease \n')
    
    plt.show()

    
def binary_heart_disease_pies(titles_lst, yes_sizes, no_sizes):
    labels = ['Have not had heart disease','Have had heart disease']
    fig, axs = plt.subplots(2, 1, figsize=(10, 12))
    axs[0].pie(yes_sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 16})
    axs[0].set_title(titles_lst[0], color='k', fontdict={'fontsize': 20})  

    axs[1].pie(no_sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 16})
    axs[1].set_title(titles_lst[1], color='k', fontdict={'fontsize': 20})  

    plt.show()
    
   
def binary_heart_disease_bars(df, feature, x_labels, legend_loc="upper left"):
    partial_df = df[['HeartDisease',feature]]

    yes_variable_df = partial_df[partial_df[feature] == 'Yes']
    heart_disease_yes_variable_counts = Counter(yes_variable_df['HeartDisease'])

    no_variable_df = partial_df[partial_df[feature] == 'No']
    heart_disease_no_variable_counts = Counter(no_variable_df['HeartDisease'])
    
    y = [len(yes_variable_df),len(no_variable_df)] 
    y1 = [heart_disease_yes_variable_counts['Yes'],heart_disease_no_variable_counts['Yes']]

    f, ax = plt.subplots(figsize=(15, 12))
    sns.barplot(x=x_labels, y=y, label='Total', color='#66c2a5')
    sns.barplot(x=x_labels, y=y1, label='Have Had Heart Disease', color='#fc8d62')
    ax.legend(ncol=2, loc=legend_loc, frameon=True)
    ax.set(ylabel='Count')
    
    plt.show()
    
    yes_variable_sizes = [heart_disease_yes_variable_counts['No'], heart_disease_yes_variable_counts['Yes']]
    no_variable_sizes = [heart_disease_no_variable_counts['No'], heart_disease_no_variable_counts['Yes']]
    
    return yes_variable_sizes,no_variable_sizes



    
    